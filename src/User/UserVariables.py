from src.common.MultiLayersVariables import MultiLayersVariables
from src.User.UserConfig import UserConfig


class UserVariables(MultiLayersVariables):

    __user_config: UserConfig = None

    def __init__(self, user_config: UserConfig):
        # Set config
        self.__user_config = user_config

        # Set variables
        self._set_raw_variables(variables=self.__user_config.variables)
