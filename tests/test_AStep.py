from unittest import TestCase

import json

from src.Step.AStep import AStep

# Step imports
from src.Step.StepConfig import StepConfig

# Workflow imports
from src.Workflow.WorkflowVariables import WorkflowVariables
from src.Workflow.WorkflowConfig import WorkflowConfig

from src.exeptions import StepInitError

from tests.test_WorkflowVariables import project_variables


# Create basic workflow variables
with open("jsons/WorkflowConfigTestWithName.json", "r") as file:
    config = json.load(file)
config = WorkflowConfig.from_dict(config)
workflow_variables = WorkflowVariables(workflow_id="test", workflow_config=config, project_variables=project_variables)

# Load the config file jsons/StepConfigTestWithName.json
with open("jsons/StepConfigTestWithName.json", "r") as file:
    config = json.load(file)
step_config_with_name = StepConfig.from_dict(config)

# Load the config file jsons/StepConfigTestWithoutName.json
with open("jsons/StepConfigTestWithoutName.json", "r") as file:
    config = json.load(file)
step_config_without_name = StepConfig.from_dict(config)


class TestStep(AStep):
    def __init__(self, step_config: StepConfig, workflow_variables: WorkflowVariables):
        super().__init__(step_config=step_config, workflow_variables=workflow_variables)

    def _execute(self):
        self.log("Test step execution")

    def _cancel(self):
        self.log("Test step cancel")


class TestAStep(TestCase):

    def test_init(self):
        step = TestStep(step_config=step_config_with_name, workflow_variables=workflow_variables)

    def test_execute(self):
        step = TestStep(step_config=step_config_with_name, workflow_variables=workflow_variables)
        step.execute()

    def test_cancel(self):
        step = TestStep(step_config=step_config_with_name, workflow_variables=workflow_variables)
        step.cancel()

    def test_init_error(self):
        with self.assertRaises(StepInitError):
            step = TestStep(step_config=step_config_with_name, workflow_variables="workflow_variables")
