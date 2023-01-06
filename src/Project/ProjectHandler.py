from src.Project.ProjectVariables import ProjectVariables
from src.Project.ProjectConfig import ProjectConfig

from src.User.UserVariables import UserVariables

from src.const import Paths, Indents

from src.exeptions import ProjectConfigError, ProjectInitError, ProjectVariablesError

from src.common.OutputWrapper import OutputWrapper

import os
import json


class ProjectHandler:

    # Output wrapper
    __output_wrapper: OutputWrapper = OutputWrapper(indent_size=Indents.PROJECT_INIT_LEVEL)

    # User variables
    __user_variables: UserVariables = None

    # Project variables
    project_variables: ProjectVariables = None

    # Project config
    project_config: ProjectConfig = None

    # Projects root
    __projects_root = Paths.PROJECTS_ROOT

    def __init__(self, project_id: str, user_variables: UserVariables):
        try:
            # Verify types
            if not isinstance(project_id, str):
                raise TypeError("Project id must be a str")
            if not isinstance(user_variables, UserVariables):
                raise TypeError("User variables must be a UserVariables")
            # Init user variables
            self.__user_variables = user_variables
            # Init project id
            self.project_id = project_id
            # Search the .json file of the project in the projects root
            list_of_files = os.listdir(self.__projects_root)
            # File path
            file_path = None
            # For each file
            for file in list_of_files:
                # Get the file name
                file_name = os.path.splitext(file)[0]
                # If the file name is the project id
                if file_name != project_id:
                    continue
                # Get the file path
                file_path = os.path.join(self.__projects_root, file)
                break
            # If the file path is None
            if file_path is None:
                self.__output_wrapper.fill("Project not found")
                raise FileNotFoundError("Project file not found")
            # Init config
            self.__init_config(file_path=file_path)
            # Init variables
            self.__init_variables()
            # End init project log
            self.__output_wrapper.fill("Project initialized")
        except Exception as e:
            self.__output_wrapper.fill(str(e))
            self.__output_wrapper.fill("Project could not be initialized")
            raise ProjectInitError(project_id=project_id) from e

    # Load the project config
    def __init_config(self, file_path: str):
        try:
            # Open the file
            with open(file_path, "r") as file:
                # Load the json
                json_data = json.load(file)
                # Create the config
                self.project_config = ProjectConfig.from_dict(json_data)
            self.__output_wrapper.fill("Project config loaded")
        except Exception as e:
            raise ProjectConfigError(project_id=self.project_id) from e

    # Init the project variables
    def __init_variables(self):
        try:
            self.project_variables = ProjectVariables(project_id=self.project_id, project_config=self.project_config, user_variables=self.__user_variables)
            self.__output_wrapper.fill("Project variables initialized")
        except Exception as e:
            raise ProjectVariablesError(project_id=self.project_id) from e

    # For test purpose: change the projects root
    def _set_projects_root(self, projects_root: str):
        self.__projects_root = projects_root

