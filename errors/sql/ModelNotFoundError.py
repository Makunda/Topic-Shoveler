class ModelNotFoundError(Exception):
    """Raised when the SQL model hasn't been found"""
    
    def __init__(self, model_path: str):
        """
        Initialize the ModelNotFound Error
        :param model_path: Path to the model file
        """
        self.message = f"Failed to retrieve the model file : {model_path}."
        super(ModelNotFoundError, self).__init__(self.message)