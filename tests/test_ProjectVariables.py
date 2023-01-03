from unittest import TestCase
import json

from src.Project.ProjectConfig import ProjectConfig
from src.Project.ProjectVariables import ProjectVariables

from src.User.UserVariables import UserVariables
from src.User.UserConfig import UserConfig

# Create valid config object with name
with open("jsons/ProjectConfigTestWithName.json", "r") as file:
    config = json.load(file)
config_with_name = ProjectConfig.from_dict(config)

# Create valid config object without name
with open("jsons/ProjectConfigTestWithoutName.json", "r") as file:
    config = json.load(file)
config_without_name = ProjectConfig.from_dict(config)

# Create basic user variables
with open("jsons/UserConfigTest.json", "r") as file:
    config = json.load(file)
config = UserConfig.from_dict(config)
user_variables = UserVariables(user_config=config)


class TestProjectVariables(TestCase):
    # Init with name
    def test_project_variables_init_with_name(self):
        # Create a project variables object
        project_variables = ProjectVariables(project_id="test_id", project_config=config_with_name,
                                             user_variables=user_variables)
        # Test name
        self.assertEqual(project_variables.project_name, "test")

    # Init without name
    def test_project_variables_init_without_name(self):
        # Create a project variables object
        project_variables = ProjectVariables(project_id="test_id", project_config=config_without_name,
                                             user_variables=user_variables)
        # Test name
        self.assertEqual(project_variables.project_name, "test_id")
