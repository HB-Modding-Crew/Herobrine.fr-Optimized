from src.User.UserVariables import UserVariables
from src.User.UserConfig import UserConfig

from src.const import Paths, Indents

from src.exeptions import UserConfigInitError, UserInitError, UserVariablesInitError

from src.common.OutputWrapper import OutputWrapper

import os
import json


class UserHandler:

    # Output wrapper
    __output_wrapper: OutputWrapper = OutputWrapper(indent_size=Indents.USER_INIT_LEVEL)

    # User path
    __user_path: str = Paths.USER_CONFIG_FILE

    # User config
    __user_config: UserConfig = None

    # User variables
    user_variables: UserVariables = None

    def __init__(self):
        try:
            # Init config
            self.__init_config()
            # Init variables
            self.__init_variables()
        except Exception as e:
            self.__output_wrapper.fill("User init error")
            self.__output_wrapper.fill(str(e))
            raise UserInitError() from e

    def __init_config(self):
        # If the user config file exists
        try:
            with open(self.__user_path, "r") as file:
                # Read the file
                file_content = file.read()
                # Try to load the file
                self.__user_config = UserConfig.from_dict(json.loads(file_content))
        except Exception as e:
            self.__output_wrapper.fill("User config init error")
            raise UserConfigInitError() from e

    def __init_variables(self):
        try:
            # Init user variables
            self.user_variables = UserVariables(user_config=self.__user_config)
        except Exception as e:
            self.__output_wrapper.fill("User variables init error")
            raise UserVariablesInitError() from e
