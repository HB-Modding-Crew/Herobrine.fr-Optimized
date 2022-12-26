from unittest import TestCase

import json

from src.User.UserVariables import UserVariables
from src.User.UserConfig import UserConfig

from src.Workflow.WorkflowVariables import WorkflowVariables
from src.Workflow.WorkflowConfig import WorkflowConfig

from src.Step.StepVariables import StepVariables
from src.Step.StepConfig import StepConfig


# Create basic user variables
with open("jsons/UserConfigTest.json", "r") as file:
    config = json.load(file)
config = UserConfig.from_dict(config)
user_variables = UserVariables(user_config=config)

# Create basic workflow variables
with open("jsons/WorkflowConfigTestWithName.json", "r") as file:
    config = json.load(file)
config = WorkflowConfig.from_dict(config)
workflow_variables = WorkflowVariables(workflow_id="test", workflow_config=config, user_variables=user_variables)

# Load the config file jsons/StepConfigTestWithName.json
with open("jsons/StepConfigTestWithName.json", "r") as file:
    config = json.load(file)
step_config_with_name = StepConfig.from_dict(config)

# Load the config file jsons/StepConfigTestWithoutName.json
with open("jsons/StepConfigTestWithoutName.json", "r") as file:
    config = json.load(file)
step_config_without_name = StepConfig.from_dict(config)


class TestStepVariables(TestCase):

    # Test init with name
    def test_step_variables_init_with_name(self):
        step_variables = StepVariables(step_config=step_config_with_name, workflow_variables=workflow_variables)
        self.assertEqual(step_variables.step_name, "test_name")

    # Test init without name
    def test_step_variables_init_without_name(self):
        step_variables = StepVariables(step_config=step_config_without_name, workflow_variables=workflow_variables)
        self.assertEqual(step_variables.step_name, "test_id")
