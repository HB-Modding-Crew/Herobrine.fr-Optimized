"""Custom exceptions for the mod pack creator."""


class ModPackCreatorError(Exception):
    """Base class for exceptions in this module."""
    pass


"""Thick config exceptions."""


class MultiLayersVariablesError(ModPackCreatorError):
    """Base class for exceptions in this module."""

    def __init__(self, actual_level_name):
        super().__init__()
        self.actual_level_name = actual_level_name

    def __str__(self):
        return f"Error in level {self.actual_level_name}."


class MultiLayersVariablesKeyError(MultiLayersVariablesError):
    """Exception raised when a key is not found in the actual level or in the precedent levels."""

    def __init__(self, actual_level_name, key):
        super().__init__(actual_level_name)
        self.key = key

    def __str__(self):
        return f"Key '{self.key}' not found in level {self.actual_level_name} or in precedent levels."


class MultiLayersVariablesReferenceError(MultiLayersVariablesError):
    """Exception raised when a reference is not found in the precedent levels."""

    def __init__(self, actual_level_name, key, precedent_key):
        super().__init__(actual_level_name)
        self.key = key

    def __str__(self):
        return f"Reference '{self.key}' to key '{self.precedent_key}' not found in precedent levels."


class MultiLayersVariablesNoPrecedentError(MultiLayersVariablesReferenceError):
    """Exception raised when a precedent variables is not defined."""

    def __init__(self, actual_level_name, key, precedent_key):
        super().__init__(actual_level_name, key, precedent_key)

    def __str__(self):
        return f"Reference '{self.key}' to key '{self.precedent_key}' not found in precedent levels because there is no precedent levels."

