from enum import Enum


class PrintColors(Enum):
    """
    Print Color for the console
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class MessageType(Enum):
    INFO = "INFO",
    ERROR = "ERROR",
    WARNING = "WARNING"


class PrintUtils:
    __module_name = ""

    @staticmethod
    def set_prefix(prefix: str):
        """
        Set a global prefix
        :param prefix: Prefix to append at the beginning of the lines
        :return:
        """
        PrintUtils.__module_name = prefix

    @staticmethod
    def error(message: str):
        """
        Print errors in red in the console
        :param message:
        :return:
        """
        PrintUtils.print_color(message, MessageType.ERROR, PrintColors.WARNING)

    @staticmethod
    def info(message: str):
        """
        Print info in blue/cyan in the console
        :param message:
        :return:
        """
        PrintUtils.print_color(message, MessageType.INFO, PrintColors.OKCYAN)

    @staticmethod
    def print_color(message: str, type: MessageType, color: PrintColors):
        """
        Print a message with  a defined color
        :param type: Type of the message to add
        :param message:  Message to print
        :param color: Color of the text
        :return:
        """
        module_name = f'{PrintUtils.__module_name} : ' if PrintUtils.__module_name else ''
        message_type = f'{type.value[0]} : '
        print(f"{message_type}{module_name}{color.value}{message}{PrintColors.ENDC.value}")
