from collections import UserString
from src.exeptions import RestrictedCharactersError
from typing import Union

# Union of normal string and UserString
AStr = Union[str, UserString]


class RestrictedStringCharacters(UserString):
    """A string that can only contain a restricted set of characters.
    """

    def __init__(self, value: AStr, allowed: str):
        """

        :param value: String value
        :param allowed: Allowed characters
        """
        super().__init__(value)
        self.allowed = allowed

        # If value contains a character that is not in allowed.
        if not all(c in allowed for c in value):
            raise RestrictedCharactersError(value, allowed)


class DisplayName(RestrictedStringCharacters):
    """A string that can only contain a restricted set of characters.
    """

    def __init__(self, value: AStr):
        """

        :param value: String value
        """
        super().__init__(value, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_ ")


class NoSpaceString(RestrictedStringCharacters):
    """A string that can only contain a restricted set of characters.
    """

    def __init__(self, value: AStr):
        """

        :param value: String value
        """
        super().__init__(value, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")