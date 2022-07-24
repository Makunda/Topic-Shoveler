class SQLConnectionError(Exception):
    """Raised when the program fails to connect to the database"""

    def __init__(self, url: str, port: int, database: str):
        self.message = f"Failed to connect to the database '{url}:{port}/{database}'."
        super(SQLConnectionError, self).__init__(self.message)