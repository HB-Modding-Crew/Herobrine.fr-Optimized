from unittest import TestCase
from src.User.UserVariables import UserVariables
from src.User.UserConfig import UserConfig

import json

with open("jsons/UserConfigTest.json", "r") as file:
    config = json.load(file)
config = UserConfig.from_dict(config)


class TestUserVariables(TestCase):

    # Test init method
    def test__init__(self):
        # Create a UserVariables instance
        variables = UserVariables(user_config=config)
        # Check if the raw variables is {"test": "test"}
        self.assertEqual(variables["test"], "test")
