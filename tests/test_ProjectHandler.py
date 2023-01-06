from unittest import TestCase

from src.Project.ProjectHandler import ProjectHandler

from test_ProjectVariables import user_variables, UserVariables


class TestProjectHandler(TestCase):

    # Test init
    def test_init(self):
        ProjectHandler(user_variables=user_variables, project_id="Test")


