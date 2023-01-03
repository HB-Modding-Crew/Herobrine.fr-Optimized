from textwrap import TextWrapper
from src.const import Indents


class OutputWrapper(TextWrapper):
    def __init__(self, ident_size: Indents):
        self.__indent = ident_size.value * "    "
        super().__init__(initial_indent=self.__indent, subsequent_indent=self.__indent)
