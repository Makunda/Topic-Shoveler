class SQLExecutionError(Exception):
    """Raised when the SQL statement fails to execute"""
    
    def __init__(self, request: str, parameters: any = None):
        """
        Initialize the SQL execution error
        :param request: SQL Request
        :param parameters: Parameters passed to the SQL statement
        """
        f_message = f"Failed to execute the query : {request}."
        if parameters:
            f_message = f"{f_message} Parameters: {parameters}."

        self.message = f_message
        super(SQLExecutionError, self).__init__(f_message)