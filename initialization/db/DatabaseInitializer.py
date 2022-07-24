import glob
import os
import re
from typing import List

from db.pg.PgConn import PgConn
from definitions import ROOT_DIR
from initialization.AbstractInitalizer import AbstractInitalizer
from logger.Logger import Logger
from secrets.Secrets import PG_BEHAVIOR, PG_MODEL_FOLDER, PG_DROP_FOLDER, PG_INIT_SCRIPT_FOLDER


class DatabaseInitializer(AbstractInitalizer):
    """
        Database initialization
        Initialize the database structure
        Declare the different init
    """

    def __init__(self):
        # Utils
        self.__logger = Logger.get_logger("Database Initializer")
        self.__pg_conn = PgConn()

        # Declare the path
        self.__init_folder = os.path.join(ROOT_DIR, PG_INIT_SCRIPT_FOLDER)
        self.__drop_folder = os.path.join(ROOT_DIR, PG_DROP_FOLDER)

        # Logger init
        self.__logger.info(f"Postgres initialization folder: {self.__init_folder}.")
        self.__logger.info(f"Postgres initialization folder: {self.__drop_folder}.")

    def parse_content(self, content: str):
        """
        Parse the content of the query and extract elements
        :param content: Content of the file
        :return:
        """
        tables = re.findall(r"CREATE TABLE(?: IF NOT EXISTS)* ([\w]+)[\s]*\(", )

    def __get_files(self, path: str, sort=True) -> List[str]:
        """
        Get the list of file
        :param path: Path of the files
        :param sort: Sort the file by name
        :return:
        """
        files: List[str] = []
        for name in glob.glob(os.path.join(path, '/*.sql')):
            files.append(name)

        # Sort the list of files
        if sort:
            files.sort()
        return files

    def __run_scripts(self, scripts: List[str]) -> None:
        """
        Execute a list of SQL scripts
        :return:
        """
        # Check if files have been discovered
        if len(scripts) == 0:
            self.__logger.warn(f"No file script has been discovered.")
            return

        # Parse the files scripts
        self.__logger.info(f"[{len(scripts)}] files scripts have been discovered.")
        for s in scripts:
            # Open the file
            with open(s) as f:
                try:
                    # Script
                    content = f.read()
                    # Execute the script
                    self.__pg_conn.execute(content)
                    self.__logger.info(f"Successfully played file [{s}].")
                except Exception as e:
                    self.__logger.error(f"Failed to execute the script [{s}].", e)
                    raise e

    def __init(self):
        """
        Launch all the initialisation services
        :return:
        """
        init_files = self.__get_files(self.__init_folder)
        self.__run_scripts(init_files)

    def __drop(self):
        """
        Launch all the drop scripts
        :return:
        """
        drop_files = self.__get_files(self.__drop_folder)
        self.__run_scripts(drop_files)

    def get_name(self):
        return "Database initialization"

    def launch(self):
        # List the mode
        self.__logger.info(f"Launched in mode: {PG_BEHAVIOR}")

        # Drop all the init
        if PG_BEHAVIOR == "DROP-AND-CREATE":
            self.__drop()
            self.__logger.info(f"Database elements were dropped.")

        # Load all the init files
        self.__init()
        self.__logger.info(f"Database elements were initialized")
