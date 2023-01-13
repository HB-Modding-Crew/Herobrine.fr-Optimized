from src.common.MultiLayersVariables import MultiLayersVariables
from src.Workflow.WorkflowVariables import WorkflowVariables
from src.Step.StepConfig import StepConfig
from src.common.StrTypes import NoSpaceString, DisplayName
from src.common.StrTypes import AStr


class StepVariables(MultiLayersVariables):

    __step_config: StepConfig = None

    def __init__(self, step_config: StepConfig, workflow_variables: WorkflowVariables):
        # Set config after verification type
        if not isinstance(step_config, StepConfig):
            raise TypeError("Step config must be a StepConfig")
        self.__step_config = step_config
        # Set id
        self.id = NoSpaceString(self.__step_config.id)
        # Set name if name is not None
        if self.__step_config.name is not None:
            self.name = DisplayName(self.__step_config.name)
        # Set type
        self.type = NoSpaceString(self.__step_config.type)
        # Precedent variables should be user variables
        if not isinstance(workflow_variables, WorkflowVariables):
            raise TypeError("Precedent variables must be a WorkflowVariables")
        # Workflow variables
        self.__workflow_variables = workflow_variables
        # Super init
        super().__init__(variables=step_config.variables, level_name="step", precedent_variables=workflow_variables)

    @property
    def step_name(self) -> str:
        # If none
        if self.__step_config.name is None:
            # Return id
            return str(self.id)
        # Else
        return str(self.name)

    @property
    def step_id(self) -> str:
        return str(self.id)

    @property
    def project_id(self) -> str:
        return str(self.__workflow_variables.project_id)

    @property
    def project_name(self) -> str:
        return str(self.__workflow_variables.project_name)

    @property
    def workflow_id(self) -> str:
        return str(self.__workflow_variables.id)

    @property
    def workflow_name(self) -> str:
        return str(self.__workflow_variables.workflow_name)
