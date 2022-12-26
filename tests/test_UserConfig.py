from unittest import TestCase
from src.User.UserConfig import UserConfig
import json


class TestUserConfig(TestCase):

    # Test valid load.
    def test_load(self):
        # Load the config file tests/jsons/UserConfigTest.json
        with open("jsons/UserConfigTest.json", "r") as file:
            config = json.load(file)
        config = UserConfig.from_dict(config)
