from typing import List


class JSONUtils:
    """
    Set of utilities for JSON
    """

    @staticmethod
    def get_value(json: dict, key: str, default=None) -> str or None:
        """
        Get the value
        :param json: Json to parse
        :param key: Key to retrieve
        :param default: (Optional) Default value to assign
        :return: The key, or none
        """
        try:
            return json[key] # Return the value
        except Exception as e:
            return default

    @staticmethod
    def get_member(json: dict, keys: List[str]):
        """
        Get the member of a json
        :throws KeyError Invalid key inside the JSON
        :return: The value of the member
        """
        try:
            if len(keys) > 1:
                k = keys.pop()
                return JSONUtils.get_member(json[k], keys) # Continue to iterate
            else:
                return json[keys[0]] # Return the value
        except Exception as e:
            raise KeyError(f"Invalid key: {'.'.join(keys)}.")
