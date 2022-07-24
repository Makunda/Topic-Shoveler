class ModelCorruptedError(Exception):
    """Raised when the SQL model hasn't been found"""
    
    def __init__(self, model_path: str):
        """
        Initialize the ModelCorrupted Error
        :param model_path: Path to the model file
        """
        self.message = f"Failed to load the model file : {model_path}. The model is corrupted."
        super(ModelCorruptedError, self).__init__(self.message)