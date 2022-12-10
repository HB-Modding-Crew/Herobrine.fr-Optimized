"""Custom exceptions for the modpack creator."""

class ModpackCreatorError(Exception):
    """Base class for exceptions in this module."""
    pass

"""Thick config exceptions."""

class MultiLayersConfigError(ModpackCreatorError):
    """Base class for exceptions in this module."""
    pass

class MultiLayersConfigReferenceError(MultiLayersConfigError):
    """Raised when a reference is not found in the precedent config."""

    def __init__(self, precedent_key: str):
        self.precedent_key = precedent_key

    def __str__(self):
        return f"Reference to precedent key '{self.precedent_key}' not found."

class MultiLayersConfigNoPrecedentError(MultiLayersConfigReferenceError):
    """Raised when a precedent config is required but not found."""

    def __init__(self, precedent_key: str):
        super().__init__(precedent_key)

    def __str__(self):
        return f"Reference to precedent key '{self.precedent_key}' not found because there is no config to refer to."