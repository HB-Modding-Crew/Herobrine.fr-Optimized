from __future__ import annotations
import re
from src.const import MultiLayersConfig as ConstMultiLayersConfig
from exeptions import MultiLayersConfigNoPrecedentError, MultiLayersConfigReferenceError

# Reference to precedent value format: "ref:precedent_key"
REF_PRECEDENT = re.compile(ConstMultiLayersConfig.REGEX_REF_PRECEDENT)


class MultiLayersConfig:

    # Init with new config json and precedent ThickConfig
    def __init__(self, config: dict, precedent: MultiLayersConfig = None):
        self._config = config
        self.precedent = precedent

    # Get attribute
    def __getattribute__(self, __name: str):
        # Match precedent reference
        match = REF_PRECEDENT.match(__name)

        # If not precedent reference
        if not match:
            # If attribute is in config
            if __name in self._config.keys():
                return self._config[__name]
            # Else verify if precedent exists
            elif self.precedent is not None:
                return self.precedent.__getattribute__(__name)
            # Else return None
            return None

        # Else if match precedent reference
        # Get precedent key
        precedent_key = match.group("key")
        # If precedent exists
        if self.precedent is not None:
            res = self.precedent.__getattribute__(precedent_key)
            if res is None:
                raise MultiLayersConfigReferenceError(precedent_key)
            return res
        # Else raise exception
        raise MultiLayersConfigNoPrecedentError(precedent_key)