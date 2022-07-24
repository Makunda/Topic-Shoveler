import base64


class StringUtils:
    """
    String utils function
    """

    @staticmethod
    def to_base64(text: str):
        """
        Convert the text into base 64
        :param text: Text to convert
        :return: The text converted to base 64
        """
        message_bytes = text.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        return base64_bytes.decode('ascii')

