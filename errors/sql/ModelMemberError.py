class ModelMemberError(Exception):
    """Raised when the value of a member is invalid"""

    def __init__(self, model_name: str, member_name: str):
        """
        Initialize the ModelCorrupted Error
        :param model_name: Name of the model
        :param member_name: Path to the model file
        """
        self.message = f"Failed process the model : {model_name}. The model is invalid, missing member: {member_name}."
        super(ModelMemberError, self).__init__(self.message)