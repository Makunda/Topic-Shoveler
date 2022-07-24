import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from enums.codes.ExitCodes import ExitCodes
from utils.PrintUtils import PrintUtils

from utils.StringUtils import StringUtils

load_dotenv()

############################################################
#                   Module Parameters                      #
############################################################
MODULE_NAME = str(os.getenv("MODULE_NAME", "ARM-CC-GO"))
PrintUtils.set_prefix(MODULE_NAME)


############################################################
#                   Server Parameters                      #
############################################################
SERVER_HOST = str(os.getenv("SERVER_HOST", "localhost"))
SERVER_PORT = int(os.getenv("SERVER_PORT", 3000))

############################################################
#                   Database Activation                    #
############################################################
DATABASE_ACTIVATION = True
DATABASE_URL = str(os.getenv('DATABASE_URL', None))
if DATABASE_URL is None:
    PrintUtils.error("ERROR: Missing DATABASE_URL parameter. The connection to database will be disabled.")
    DATABASE_ACTIVATION = False

DATABASE_PORT = str(os.getenv('DATABASE_PORT', None))
if DATABASE_PORT is None:
    PrintUtils.error("ERROR: Missing DATABASE_PORT parameter. The connection to database will be disabled.")
    DATABASE_ACTIVATION = False

DATABASE_NAME = str(os.getenv('DATABASE_NAME', None))
if DATABASE_NAME is None:
    PrintUtils.error("ERROR: Missing DATABASE_NAME parameter. The connection to database will be disabled.")
    DATABASE_ACTIVATION = False

DATABASE_USERNAME = str(os.getenv('DATABASE_USERNAME', None))
if DATABASE_USERNAME is None:
    PrintUtils.error("ERROR: Missing DATABASE_USERNAME parameter. The connection to database will be disabled.")
    DATABASE_ACTIVATION = False

DATABASE_PASSWORD = str(os.getenv('DATABASE_PASSWORD', None))
if DATABASE_PASSWORD is None:
    PrintUtils.error("ERROR: Missing DATABASE_PASSWORD parameter. The connection to database will be disabled.")
    DATABASE_ACTIVATION = False

__temp_encryption = str(os.getenv('DATABASE_ENCRYPTION', None))
DATABASE_ENCRYPTION = __temp_encryption == 'True' or __temp_encryption == 'y' or __temp_encryption == 'yes'
if DATABASE_ENCRYPTION is None:
    PrintUtils.error("ERROR: Missing DATABASE_ENCRYPTION parameter. The connection to database will be disabled.")
    DATABASE_ACTIVATION = False

if not DATABASE_ACTIVATION:
    PrintUtils.error("The database has not been activated. The system will now stop.")
    sys.exit(ExitCodes.DATABASE_NOT_ACTIVATED)

PrintUtils.info("Valid database configuration discovered.")


############################################################
#                  Logger Configuration                    #
############################################################
LOGGER_NAME = os.getenv('LOGGER_NAME', None)
if LOGGER_NAME is None:
    PrintUtils.error(f"Missing LOGGER_NAME parameters. Falling back to default: [{MODULE_NAME}].")
    LOGGER_NAME = MODULE_NAME

LOG_FOLDER = os.getenv('LOG_FOLDER', None)
if LOG_FOLDER is None:
    log_path = Path.home().joinpath(f'{MODULE_NAME}/logs/')
    try:
        if not log_path.exists():
            os.makedirs(log_path)
        LOG_FOLDER = str(log_path)
    except:
        PrintUtils.error(f"Failed to create the log folder at [{log_path}]."
                         f" Make sure this folder is accessible or specify the LOG_FOLDER parameter in .env file.")

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

############################################################
#                 Postgres Configuration                   #
############################################################
PG_INIT_SCRIPT_FOLDER = str(os.getenv('PG_INIT_SCRIPT_FOLDER', 'queries/init/'))
PG_MODEL_FOLDER = str(os.getenv('PG_MODEL_FOLDER', 'queries/models/'))
PG_DROP_FOLDER = str(os.getenv('PG_DROP_FOLDER', 'queries/drop/'))

PG_BEHAVIOR = str(os.getenv('PG_BEHAVIOR', 'NONE'))
