import logging
import os
from logging.handlers import RotatingFileHandler

from metaclass.SingletonMeta import SingletonMeta
from secrets.Secrets import LOG_FOLDER, LOG_LEVEL
from utils.FolderUtils import FolderUtils


class Logger(metaclass=SingletonMeta):
    """
    Singleton class in charge of wrapping the default logger
    """

    _log_folder = ""
    _log_level = ""
    _log_path = ""

    def get_log_path(self):
        return self._log_path

    def __init__(self):
        """
        Initialize logging and displays information
        :return: None
        """
        self._log_folder = str(LOG_FOLDER)
        self._log_level = str(LOG_LEVEL)

        # Create log folder if needed
        self._log_path = os.path.join(self._log_folder)
        FolderUtils.merge_folder(self._log_path)

        os.chmod(self._log_path, 0o777)

        # Print log files and level
        message = "Logs will be saved to {0}. Log level is: {1}".format(self._log_folder, self._log_level)
        logging.debug(message)

        timestamp = ""

        # define logs files and folders
        info_file = "BitBulket_info" + timestamp + ".log"
        self.__log_file = os.path.join(self._log_folder, info_file)

        error_file = "BitBulket_error" + timestamp + ".log"
        self.__error_file = os.path.join(self._log_folder, error_file)

        self.__log_handler = RotatingFileHandler(self.__log_file, maxBytes=1048576, backupCount=5)
        self.__log_handler.setFormatter(
            logging.Formatter('%(asctime)s %(levelname)s : %(message)s ' '[in %(pathname)s:%(lineno)d]'))

    def get_logging_path(self) -> str:
        """
        Get the logging folder path
        :return: The path of the folder
        """
        return str(self._log_folder)

    def get(self, name) -> logging.Logger:
        """
        Get a logger with a prefixed name
        :param name:  Name of the logger
        :return: The logger Wrapped
        """
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(self.__log_handler)
        return logger

    @staticmethod
    def get_logger(name):
        logger = Logger()
        return logger.get(name)
