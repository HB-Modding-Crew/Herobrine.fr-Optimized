from src.Step.AStep import AStep
from src.exeptions import MultiLayersVariablesNoPrecedentError, MultiLayersVariablesReferenceError


# Step class is a step that can be used in a workflow
class Step(AStep):
    # Constructor
    def __init__(self, id: str, step_config: dict):
        # Call super constructor
        super().__init__(id, step_config)

    # Actions to execute when the step is executed
    def _execute(self) -> bool:
        # Try to get configs
        try:
            # Get project name
            project_name = self.var
            # Get step name
            step_name = "test_name"
            # Print execution of the step
            self.log("Executing step '" + step_name + "' of project '" + project_name + "'")
            return True
        except MultiLayersVariablesNoPrecedentError as e:
            # If no precedent config, raise exception
            self.log(f"Trying to get {e.precedent_key} of precedent config level from {e.config_level_name} but there is no precedent config level")
        except MultiLayersVariablesReferenceError as e:
            # If key not found in precedent config
            self.log(f"Trying to get {e.precedent_key} of precedent config level {e.precedent_config_level_name} from {e.config_level_name} but {e.precedent_key} is not found in {e.precedent_config_level_name}")
        except KeyError as e:
            # If key not found in config
            self.log(f"Trying to get {e} from config but {e} is not found in config")
        # Return false if an error occurred
        return False

    # Actions to execute when the step is canceled
    def _cancel(self):
        self.log("TestStep cancellation")
