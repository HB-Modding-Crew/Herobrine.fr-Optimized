from unittest import TestCase
import json

from src.Step.StepConfig import StepConfig


class TestStepConfig(TestCase):

    def test_from_dict_with_name(self):
        # Load the config file jsons/StepConfigTestWithName.json
        with open("jsons/StepConfigTestWithName.json", "r") as file:
            config = json.load(file)
        config = StepConfig.from_dict(config)
        # Test name
        self.assertEqual(config.name, "test_name")

    def test_from_dict_without_name(self):
        # Load the config file jsons/StepConfigTestWithoutName.json
        with open("jsons/StepConfigTestWithoutName.json", "r") as file:
            config = json.load(file)
        config = StepConfig.from_dict(config)
        # Test name
        self.assertEqual(config.name, None)
