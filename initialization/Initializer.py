from typing import List

from initialization.AbstractInitalizer import AbstractInitalizer
from initialization.db.DatabaseInitializer import DatabaseInitializer
from logger.Logger import Logger


class Initializer:
    """
    Initializing class
    """

    def __init__(self):
        """
        Initializer
        """
        self.__logger = Logger.get_logger("Initializer")
        # List of init files to take in account
        self.__init_list: List[AbstractInitalizer] = [
            DatabaseInitializer()
        ]

    def launch(self):
        """
        Launch all the initializers
        :return:
        """
        it = 0
        total_service = len(self.__init_list)

        self.__logger.info(f"Launching the {total_service} initializer services")

        for x in self.__init_list:
            it += 1

            try:
                self.__logger.info(f"[{it}/{total_service}] Processing: {x.get_name()}.")
                x.launch()
            except Exception as e:
                self.__logger.error(f"[{it}/{total_service}] Failed: {x.get_name()}.")
                self.__logger.error(e)

