from src.common.MultiLayersVariables import MultiLayersVariables
from src.Project.ProjectConfig import ProjectConfig
from src.User.UserVariables import UserVariables
from src.common.StrTypes import NoSpaceString, DisplayName
from src.common.StrTypes import AStr


class ProjectVariables(MultiLayersVariables):

    __project_config: ProjectConfig = None
    id: NoSpaceString = None
    __name: DisplayName = None

    def __init__(self, project_id: str, project_config: ProjectConfig, user_variables: UserVariables):
        # Set config after verification type
        if not isinstance(project_config, ProjectConfig):
            raise TypeError("Workflow config must be a WorkflowConfig")
        self.__project_config = project_config
        # Set id
        self.id = NoSpaceString(project_id)
        # Set name if name is not None
        if self.__project_config.name is not None:
            self.__name = DisplayName(self.__project_config.name)
        # Precedent variables should be user variables
        if not isinstance(user_variables, UserVariables):
            raise TypeError("User variables must be a UserVariables")
        # Super init
        super().__init__(variables=project_config.variables, level_name="workflow", precedent_variables=user_variables)

    @property
    def project_name(self) -> AStr:
        # If none
        if self.__project_config.name is None:
            # Return id
            return self.id
        # Else
        return self.__project_config.name
