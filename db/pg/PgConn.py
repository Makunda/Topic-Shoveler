from typing import List

import psycopg2

from errors.sql.SQLConnectionError import SQLConnectionError
from errors.sql.SQLExecutionError import SQLExecutionError
from logger.Logger import Logger
from metaclass.SingletonMeta import SingletonMeta
from secrets.Secrets import DATABASE_URL, DATABASE_PORT, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_NAME


class PgConn(metaclass=SingletonMeta):
    """
    Postgres database connection
    """

    def __init__(self):
        """
        Initialize the PG admin connection layer
        """
        # Initialize logger
        self.__logger = Logger.get_logger("PgConn")
        # Open and keep the connection
        try:
            self.__conn = psycopg2.connect(dbname=DATABASE_NAME,
                                           host=DATABASE_URL,
                                           port=DATABASE_PORT,
                                           user=DATABASE_USERNAME,
                                           password=DATABASE_PASSWORD)
        except Exception as e:
            self.__logger.error("Failed to connect to the pg database.", e)
            raise SQLConnectionError(DATABASE_URL, DATABASE_PORT, DATABASE_NAME)

    def test_connection(self) -> bool:
        """
        Test the connection
        :return: True if the test is successful
        """
        request = "SELECT 1"
        try:
            self.execute(request)
            return True
        except Exception as e:
            self.__logger.error(f"Failed to execute the test statement.", e)
            raise SQLExecutionError(request)

    def execute(self, query: str, params: tuple = None) -> List:
        """
        Execute a native SQL statement
        :param query: Query to execute
        :param params: (Optional) List of parameters
        :throws SQLExecutionError If the query fails
        :return: Records of the query
        """
        with self.__conn.cursor() as cur:
            try:
                # Handle params
                if params:
                    cur.execute(query, params)
                else:
                    cur.execute(query)

                values = []
                for record in cur:
                    values.append(record)

                return values
            except Exception as e:
                self.__logger.error(f"Failed to execute the statement: {query}", e)
                raise SQLExecutionError(query, params)

    def __del__(self):
        """
        Make sure to close the connection if the object is deleted
        :return:
        """
        try:
            if self.__conn and self.__conn:
                self.__conn.close()
        except:
            pass
