from src.common.MultiLayersVariables import MultiLayersVariables
from src.Workflow.WorkflowConfig import WorkflowConfig
from src.Project.ProjectVariables import ProjectVariables
from src.common.StrTypes import NoSpaceString, DisplayName
from src.common.StrTypes import AStr
from src.Step.StepConfig import StepConfig
from typing import List


class WorkflowVariables(MultiLayersVariables):

    __workflow_config: WorkflowConfig = None
    id: NoSpaceString = None
    __name: DisplayName = None

    def __init__(self, workflow_id: str, workflow_config: WorkflowConfig, project_variables: ProjectVariables):
        # Set config after verification type
        if not isinstance(workflow_config, WorkflowConfig):
            raise TypeError("Workflow config must be a WorkflowConfig")
        self.__workflow_config = workflow_config
        # Set id
        self.id = NoSpaceString(workflow_id)
        # Set name if name is not None
        if self.__workflow_config.name is not None:
            self.__name = DisplayName(self.__workflow_config.name)
        # Precedent variables should be user variables
        if not isinstance(project_variables, ProjectVariables):
            raise TypeError("User variables must be a UserVariables")
        self.__project_variables = project_variables
        # Super init
        super().__init__(variables=workflow_config.variables, level_name="workflow", precedent_variables=project_variables)

    @property
    def workflow_name(self) -> AStr:
        # If none
        if self.__workflow_config.name is None:
            # Return id
            return self.id
        # Else
        return self.__workflow_config.name

    @property
    def workflow_steps(self) -> List[StepConfig]:
        return self.__workflow_config.steps

    @property
    def project_id(self) -> NoSpaceString:
        return self.__project_variables.id

    @property
    def project_name(self) -> AStr:
        return self.__project_variables.project_name
