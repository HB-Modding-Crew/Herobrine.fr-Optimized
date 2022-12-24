from __future__ import annotations
from typing import Dict, Any
import re

from src.exeptions import MultiLayersVariablesKeyError, MultiLayersVariablesReferenceError, MultiLayersVariablesNoPrecedentError

from src.const import MultiLayersVariables as MultiLayersVariablesConfig

# Init reference regex
reference_regex = re.compile(MultiLayersVariablesConfig.REGEX_REF_PRECEDENT)


class MultiLayersVariables:
    """ Multi layers configuration class.
    """

    __raw_variables: Dict[str, Any]
    __precedent_variables: MultiLayersVariables
    __level_name: str

    def __init__(self, variables: Dict[str, Any], level_name: str, precedent_variables: MultiLayersVariables = None):
        """
        Constructor

        :param variables: Raw variables
        :param level_name: Level name
        :param precedent_variables: Precedent variables
        """

        # If precedent variables is defined.
        if precedent_variables is not None:
            # If precedent variables is not a MultiLayersVariables instance.
            if not isinstance(precedent_variables, MultiLayersVariables):
                raise TypeError("Precedent variables must be a MultiLayersVariables instance.")
            # Set precedent variables.
            self.__precedent_variables = precedent_variables

        # Set level name.
        self._set_level_name(level_name)

        # Set raw variables.
        self._set_raw_variables(variables)

    def _set_raw_variables(self, variables: Dict[str, Any]):
        """
        Set raw variables
        :param variables: Raw variables
        :return:
        """

        # Set raw variables.
        self.__raw_variables = variables

    def _set_precedent_variables(self, precedent_variables: MultiLayersVariables):
        """
        Set precedent variables
        :param precedent_variables: Precedent variables
        :return:
        """

        # Set precedent variables.
        self.__precedent_variables = precedent_variables

    def _set_level_name(self, level_name: str):
        """
        Set level name
        :param level_name: Level name
        :return:
        """

        # Set level name.
        self.__level_name = level_name

    def __getitem__(self, item: str) -> Any:
        """
        Get item from actual level or precedents levels.
        :param item: Item to get
        :return:
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
                raise MultiLayersVariablesNoPrecedentError(_in_precedent_variables, self.__level_name)
            # Else raise key error.
            raise MultiLayersVariablesKeyError(_in_precedent_variables, self.__level_name)
        # Try to get item from precedent variables.
        try:
            return self.__precedent_variables[_in_precedent_variables]
        except MultiLayersVariablesKeyError as e:
            # If it is a reference.
            if _ref:
                # Raise reference error.
                raise MultiLayersVariablesReferenceError(_in_precedent_variables, self.__level_name) from e
            # Else raise key error.
            raise MultiLayersVariablesKeyError(_in_precedent_variables, self.__level_name) from e
