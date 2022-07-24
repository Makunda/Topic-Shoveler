from abc import ABC, abstractmethod


class AbstractInitalizer(ABC):
    """
    Abstract initializer
    """

    @abstractmethod
    def get_name(self):
        """
        Get the name of the process
        :return:
        """
        pass

    @abstractmethod
    def launch(self):
        """
        Launch the initialization process
        :return:
        """