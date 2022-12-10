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

    def __init__(self, precedent_key: str, config_level_name: str, precedent_config_level_name: str):
        config_level_name = config_level_name
        self.precedent_key = precedent_key
        precedent_config_level_name = precedent_config_level_name

    def __str__(self):
        return f"Reference to precedent key '{self.precedent_key}' from config '{self.config_level_name}' not found in precedent config '{self.precedent_config_level_name}'."

class MultiLayersConfigNoPrecedentError(MultiLayersConfigError):
    """Raised when a precedent config is required but not found."""

    def __init__(self, precedent_key: str, config_level_name: str):
        config_level_name = config_level_name
        self.precedent_key = precedent_key

    def __str__(self):
        return f"Reference to precedent key '{self.precedent_key}' from config '{self.config_level_name}' not found because there is no precedent config."