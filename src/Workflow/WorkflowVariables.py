from src.common.MultiLayersVariables import MultiLayersVariables
from src.Workflow.WorkflowConfig import WorkflowConfig
from src.User.UserVariables import UserVariables
from src.common.StrTypes import NoSpaceString, DisplayName
from src.common.StrTypes import AStr


class WorkflowVariables(MultiLayersVariables):

    __workflow_config: WorkflowConfig = None
    id: NoSpaceString = None
    __name: DisplayName = None

    def __init__(self, workflow_id: str, workflow_config: WorkflowConfig, user_variables: UserVariables):
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
        if not isinstance(user_variables, UserVariables):
            raise TypeError("User variables must be a UserVariables")
        # Super init
        super().__init__(variables=workflow_config.variables, level_name="workflow", precedent_variables=user_variables)

    @property
    def workflow_name(self) -> AStr:
        # If none
        if self.__workflow_config.name is None:
            # Return id
            return self.id
        # Else
        return self.__workflow_config.name
