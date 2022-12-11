from __future__ import annotations
import re
from src.const import MultiLayersConfig as ConstMultiLayersConfig
from src.exeptions import MultiLayersConfigNoPrecedentError, MultiLayersConfigReferenceError

# Reference to precedent value format: "ref:precedent_key"
REF_PRECEDENT = re.compile(ConstMultiLayersConfig.REGEX_REF_PRECEDENT)


class MultiLayersConfig:

    # Init with new config json and precedent ThickConfig
    def __init__(self, config: dict, config_level_name: str, precedent: MultiLayersConfig = None):
        self._config = config
        self.precedent = precedent
        self.config_level_name = config_level_name

    # Get attribute
    def __getattribute__(self, __name: str):
        # Verify if attribute is in config
        if not __name in self._config.keys():
            # If no precedent
            if self.precedent is None:
                return None
            # Else return precedent value for __name
            return self.precedent.__getattribute__(__name)

        # Match precedent reference
        # Default false
        match = False
        # If value is string
        if isinstance(self._config[__name], str):
            # Try to match precedent reference
            match = REF_PRECEDENT.match(self._config[__name])

        # If not precedent reference
        if not match:
            # Return config value
            return self._config[__name]

        # Else if match precedent reference
        # Get precedent key
        precedent_key = match.group("key")
        # If precedent exists
        if self.precedent is not None:
            res = self.precedent.__getattribute__(precedent_key)
            if res is None:
                raise MultiLayersConfigReferenceError(precedent_key, self.config_level_name, self.precedent.config_level_name)
            return res
        # Else raise exception
        raise MultiLayersConfigNoPrecedentError(precedent_key, self.config_level_name)