from unittest import TestCase
import json
from src.Workflow.WorkflowConfig import WorkflowConfig


class TestWorkflowConfig(TestCase):

    def test_from_dict_with_name(self):
        # Load the config file jsons/WorkflowConfigTestWithName.json
        with open("jsons/WorkflowConfigTestWithName.json", "r") as file:
            config = json.load(file)
        config = WorkflowConfig.from_dict(config)
        # Test name
        self.assertEqual(config.name, "test")

    def test_from_dict_without_name(self):
        # Load the config file jsons/WorkflowConfigTestWithoutName.json
        with open("jsons/WorkflowConfigTestWithoutName.json", "r") as file:
            config = json.load(file)
        config = WorkflowConfig.from_dict(config)
        # Test name
        self.assertEqual(config.name, None)

