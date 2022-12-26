from src.common.MultiLayersVariables import MultiLayersVariables
from src.Step.StepConfig import StepConfig
from src.common.StrTypes import NoSpaceString, DisplayName
from src.common.StrTypes import AStr


class StepVariables(MultiLayersVariables):

    __step_config: StepConfig = None

    def __init__(self, step_config: StepConfig, workflow_variables: MultiLayersVariables):
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
        if not isinstance(workflow_variables, MultiLayersVariables):
            raise TypeError("Precedent variables must be a MultiLayersVariables")
        # Super init
        super().__init__(variables=step_config.variables, level_name="step", precedent_variables=workflow_variables)

    @property
    def step_name(self) -> AStr:
        # If none
        if self.__step_config.name is None:
            # Return id
            return self.id
        # Else
        return self.name
