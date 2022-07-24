class ModelInvalidError(Exception):
    """Raised when the SQL model hasn't been found"""

    def __init__(self, model_path: str, missing_key: str):
        """
        Initialize the ModelCorrupted Error
        :param model_path: Path to the model file
        """
        self.message = f"Failed to load the model file : {model_path}. The model is invalid, missing key : {missing_key}."
        super(ModelInvalidError, self).__init__(self.message)