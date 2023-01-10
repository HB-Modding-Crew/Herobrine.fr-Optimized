from typing import Union

# User imports
from src.User.UserHandler import UserHandler

# Project imports
from src.Project.ProjectHandler import ProjectHandler

# Workflow imports
from src.Workflow.Workflow import Workflow
from src.Workflow.WorkflowConfig import WorkflowConfig

# Const imports
from src.const import Indents, Paths

# Common imports
from src.common.OutputWrapper import OutputWrapper

# Exception imports
from src.exeptions import ModPackCreatorInitError, ModPackCreatorExecutionInitError

# Utils imports
import json


class Creator:

    # Output wrapper
    __output_wrapper = OutputWrapper(indent_size=Indents.COMMAND_LEVEL)

    # User handler (UserHandler or None)
    __user_handler: Union[UserHandler, None] = None

    def __init__(self):
        try:
            # Init user handler
            self.__user_handler = UserHandler()
            # Log success
            self.__output_wrapper.fill("ModpackCreator init success")
        except Exception as e:
            self.__output_wrapper.fill("ModpackCreator init failed")
            raise ModPackCreatorInitError() from e

    def execute(self, project_id: str, workflow_id: str):
        try:
            # Init project handler
            print(self.__output_wrapper.fill("Init project handler:"))
            project_handler = ProjectHandler(project_id=project_id, user_variables=self.__user_handler.user_variables)
            print(self.__output_wrapper.fill("Project initialized"))

            # Init workflow
            print(self.__output_wrapper.fill("Init workflow:"))
            workflow_config_path = Paths.WORKFLOWS_ROOT + Paths.SEPARATOR + workflow_id + Paths.EXTENSION_JSON
            with open(workflow_config_path, "r") as workflow_config_file:
                workflow_config = WorkflowConfig.from_dict(json.load(workflow_config_file))
            workflow = Workflow(workflow_id=workflow_id, workflow_config=workflow_config, project_variables=project_handler.project_variables)
            print(self.__output_wrapper.fill("Workflow initialized"))
        except Exception as e:
            print(self.__output_wrapper.fill("ModpackCreator execution init failed"))
            raise ModPackCreatorExecutionInitError() from e

        # Execute workflow
        try:
            # Workflow execution
            print(self.__output_wrapper.fill("Workflow execution:"))
            workflow.execute()
            print(self.__output_wrapper.fill("Workflow execution success"))
        except Exception as e:
            print(self.__output_wrapper.fill("Workflow execution failed"))
            raise e
