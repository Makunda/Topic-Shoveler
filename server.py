# Import utils
import sys

# Enum and logging
from enums.codes.ExitCodes import ExitCodes
from utils.PrintUtils import PrintUtils


def launch_server():
    # Launching
    from secrets.Secrets import SERVER_PORT, SERVER_HOST

    # Launch Flask server
    try:
        from server import app
        app.run(SERVER_HOST, port=SERVER_PORT)
    except Exception as e:
        PrintUtils.error(f"Failed to start the web server. Error: {e}")
        sys.exit(ExitCodes.FLASK_SERVER_INVALID)
        # Execution stops here


def initialize_logger():
    """
    Instantiate the logger
    :return: Logger
    """
    from logger.Logger import Logger
    try:
        logger = Logger.get_logger("Server")
        return logger
    except Exception as e:
        PrintUtils.error(f"Failed to instantiate the logger. Error: {e}")
        sys.exit(ExitCodes.LOGGER_NOT_INSTANTIATED)


def initialize_database():
    """
    Initialize the database
    :return: The database connector
    """
    from db.pg.PgConn import PgConn
    try:
        pg_conn = PgConn()
        pg_conn.test_connection()
        return pg_conn
    except Exception as e:
        PrintUtils.error(f"Failed to connect to the database. Error: {e}")
        sys.exit(ExitCodes.DATABASE_NOT_CONNECTED)


def initialize_services():
    """
    Initialize all the services.
    Database, etc...
    """
    try:
        from initialization.Initializer import Initializer
        initializer = Initializer()
        initializer.launch()
    except Exception as e:
        PrintUtils.error(f"Failed to initialize the modules. Error: {e}")
        sys.exit(ExitCodes.INITIALIZATION_FAILED)


def main():
    """
    Program entry point
    :return:
    """
    # Verify the configuration

    # Import secrets
    PrintUtils.info("Loading secrets...")
    PrintUtils.info("Secrets loaded")

    # Logging configuration
    PrintUtils.info("Loading logger...")
    logger = initialize_logger()

    # Testing the connection with the database
    logger.info("Opening a connection to the database...")
    initialize_database()
    logger.info(f"Connection to the database successful")

    # Load the services
    logger.info("Initialize services..")
    initialize_services()

    # Launch initialization
    logger.info("Launching the flask server..")
    launch_server()


if __name__ == '__main__':
    main()
