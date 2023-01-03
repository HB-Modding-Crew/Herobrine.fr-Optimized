from unittest import TestCase
import json

from src.Workflow.WorkflowConfig import WorkflowConfig
from src.Workflow.WorkflowVariables import WorkflowVariables
from src.Project.ProjectVariables import ProjectVariables
from src.Project.ProjectConfig import ProjectConfig

from tests.test_ProjectVariables import user_variables

# Create valid config object with name
with open("jsons/WorkflowConfigTestWithName.json", "r") as file:
    config = json.load(file)
config_with_name = WorkflowConfig.from_dict(config)

# Create valid config object without name
with open("jsons/WorkflowConfigTestWithoutName.json", "r") as file:
    config = json.load(file)
config_without_name = WorkflowConfig.from_dict(config)

# Create basic project variables
with open("jsons/ProjectConfigTestWithName.json", "r") as file:
    config = json.load(file)
config = ProjectConfig.from_dict(config)
project_variables = ProjectVariables(project_id="test_id", project_config=config, user_variables=user_variables)


class TestWorkflowVariables(TestCase):
    def test_workflow_variables_init_with_name(self):
        # Create a workflow variables object
        workflow_variables = WorkflowVariables(workflow_id="test_id", workflow_config=config_with_name,
                                               project_variables=project_variables)
        # Test name
        self.assertEqual(workflow_variables.workflow_name, "test")

    def test_workflow_variables_init_without_name(self):
        # Create a workflow variables object
        workflow_variables = WorkflowVariables(workflow_id="test_id", workflow_config=config_without_name,
                                               project_variables=project_variables)
        # Test name
        self.assertEqual(workflow_variables.workflow_name, "test_id")
