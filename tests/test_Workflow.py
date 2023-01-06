from unittest import TestCase
import json

from src.Workflow.Workflow import Workflow
from src.Step.StepTypesManager import StepTypesManager

from src.Workflow.WorkflowConfig import WorkflowConfig
from src.Workflow.WorkflowVariables import WorkflowVariables

from src.Project.ProjectVariables import ProjectVariables
from src.Project.ProjectConfig import ProjectConfig

from tests.test_StepVariables import StepVariables
from tests.test_StepConfig import StepConfig

from tests.test_WorkflowVariables import project_variables, config_with_name, config_without_name


class TestWorkflow(TestCase):

    def test_init(self):
        StepTypesManager.set_steps_path("example_steps_functional")
        StepTypesManager.load_steps_types()
        Workflow(workflow_id="test_id", workflow_config=config_with_name, project_variables=project_variables)

    def test_execute(self):
        StepTypesManager.set_steps_path("example_steps_functional")
        StepTypesManager.load_steps_types()
        workflow = Workflow(workflow_id="test_id", workflow_config=config_with_name, project_variables=project_variables)

        # Test execute
        workflow.execute()

    def test_cancel(self):
        StepTypesManager.set_steps_path("example_steps_functional")
        StepTypesManager.load_steps_types()
        workflow = Workflow(workflow_id="test_id", workflow_config=config_with_name, project_variables=project_variables)

        # Test cancel
        workflow.cancel()
