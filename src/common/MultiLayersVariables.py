from __future__ import annotations
from typing import Dict, Any
import re

from src.exeptions import MultiLayersVariablesKeyError, MultiLayersVariablesReferenceError, MultiLayersVariablesNoPrecedentError, MultiLayersVariablesInitError

from src.const import MultiLayersVariables as MultiLayersVariablesConfig

from src.common.StrTypes import DisplayName

# Init reference regex
reference_regex = re.compile(MultiLayersVariablesConfig.REGEX_REF_PRECEDENT)


class MultiLayersVariables:
    """ Multi layers configuration class.
    """

    __raw_variables: Dict[str, Any] = None
    __precedent_variables: MultiLayersVariables = None
    __level_name: DisplayName = None

    def __init__(self, variables: Dict[str, Any], level_name: str, precedent_variables: MultiLayersVariables = None):
        """
        Constructor

        :param variables: Raw variables
        :param level_name: Level name
        :param precedent_variables: Precedent variables
        """

        try:
            # If precedent variables is defined.
            if precedent_variables is not None:
                # Set precedent variables.
                self._set_precedent_variables(precedent_variables)

            # Set level name.
            self._set_level_name(level_name)

            # Set raw variables.
            self._set_raw_variables(variables)
        except Exception as e:
            raise MultiLayersVariablesInitError(level_name) from e

    def _set_raw_variables(self, variables: Dict[str, Any]):
        """
        Set raw variables
        :param variables: Raw variables
        :return:
        """

        # Verify if variables is a dict.
        if not isinstance(variables, dict):
            raise TypeError("Variables must be a dict")
        # Set raw variables.
        self.__raw_variables = variables

    def _set_precedent_variables(self, precedent_variables: MultiLayersVariables):
        """
        Set precedent variables
        :param precedent_variables: Precedent variables
        :return:
        """

        # Verify if precedent variables is a MultiLayersVariables.
        if not isinstance(precedent_variables, MultiLayersVariables):
            raise TypeError("Precedent variables must be a MultiLayersVariables")
        # Set precedent variables.
        self.__precedent_variables = precedent_variables

    def _set_level_name(self, level_name: str):
        """
        Set level name
        :param level_name: Level name
        :return:
        """

        # Verify if level name is a str.
        if not isinstance(level_name, str):
            raise TypeError("Level name must be a str")

        # Set level name.
        self.__level_name = DisplayName(level_name)

    def __getitem__(self, item: str) -> Any:
        """
        Get item from actual level or precedents levels.
        :param item: Item to get
        :return: Value of the item
        """

        _in_precedent_variables: str = None
        _ref: bool = False

        # If item in actual variables.
        if item in self.__raw_variables.keys():
            # Get item.
            _item = self.__raw_variables[item]
            # Get matched item.
            match = reference_regex.match(_item)
            # If item is a reference.
            if match:
                # Get reference name.
                _in_precedent_variables = match.group(1)
            else:
                # Try to get item.
                try:
                    return self.__raw_variables[item]
                except KeyError:
                    pass

        # if _is_in_precedent_variables is None, set with item. Else, it is a reference.
        if _in_precedent_variables is None:
            _in_precedent_variables = item
        else:
            _ref = True

        # Verify if precedent variables are defined.
        if self.__precedent_variables is None:
            # If it is a reference.
            if _ref:
                # Raise no precedent exception.
                raise MultiLayersVariablesNoPrecedentError(self.__level_name, item, _in_precedent_variables)
            # Else raise key error.
            raise MultiLayersVariablesKeyError(self.__level_name, item)
        # Try to get item from precedent variables.
        try:
            return self.__precedent_variables[_in_precedent_variables]
        except MultiLayersVariablesKeyError as e:
            # If it is a reference.
            if _ref:
                # Raise reference error.
                raise MultiLayersVariablesReferenceError(self.__level_name, item, _in_precedent_variables) from e
            # Else raise key error.
            raise MultiLayersVariablesKeyError(self.__level_name, item) from e
