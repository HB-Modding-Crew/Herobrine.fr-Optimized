from unittest import TestCase
import json

from src.Workflow.WorkflowConfig import WorkflowConfig
from src.Workflow.WorkflowVariables import WorkflowVariables
from src.User.UserVariables import UserVariables
from src.User.UserConfig import UserConfig


# Create valid config object with name
with open("jsons/WorkflowConfigTestWithName.json", "r") as file:
    config = json.load(file)
config_with_name = WorkflowConfig.from_dict(config)

# Create valid config object without name
with open("jsons/WorkflowConfigTestWithoutName.json", "r") as file:
    config = json.load(file)
config_without_name = WorkflowConfig.from_dict(config)

# Create basic user variables
with open("jsons/UserConfigTest.json", "r") as file:
    config = json.load(file)
config = UserConfig.from_dict(config)
user_variables = UserVariables(user_config=config)


class TestWorkflowVariables(TestCase):
    def test_workflow_variables_init_with_name(self):
        # Create a workflow variables object
        workflow_variables = WorkflowVariables(workflow_id="test_id", workflow_config=config_with_name, user_variables=user_variables)
        # Test name
        self.assertEqual(workflow_variables.workflow_name, "test")

    def test_workflow_variables_init_without_name(self):
        # Create a workflow variables object
        workflow_variables = WorkflowVariables(workflow_id="test_id", workflow_config=config_without_name, user_variables=user_variables)
        # Test name
        self.assertEqual(workflow_variables.workflow_name, "test_id")
