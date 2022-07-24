from enum import Enum


class ExitCodes(Enum):
    """
    List of exit codes of the application
    """
    DATABASE_NOT_ACTIVATED = 10001,
    DATABASE_NOT_CONNECTED = 10002
    HIGHLIGHT_NOT_ACTIVATED = 20001,
    LOGGER_NOT_INSTANTIATED = 30001,
    INITIALIZATION_FAILED = 40001,
    FLASK_SERVER_INVALID = 50001,
