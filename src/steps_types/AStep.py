from src.const import Steps
from src.common.MultiLayersConfig import MultiLayersConfig

# Non instanciable Abstract class AStep
# This class is the base class for all steps
# A step can be used in a workflow
class AStep:
    def __init__(self, id: str, step_config: dict):
        # Step id
        self.id = id
        # Step config
        # Verify that the step config contains the step id
        if self.id in step_config:
            self.config = step_config

        # Step id can only contain lower alphanumeric characters
        if not self.id.isalnum() or not self.id.islower():
            raise Exception("Invalid step id: '" + self.id + "'. Only lower alphanumeric characters are allowed.")

    # Actions to execute when the step is executed
    def _execute(self, config: MultiLayersConfig):
        # OVERRIDE THIS METHOD TO EXECUTE THE STEP
        pass

    # Actions to execute when the step is canceled
    def _cancel(self, config: MultiLayersConfig):
        # OVERRIDE THIS METHOD TO CANCEL THE STEP
        pass

    # Called when execution of the step is requested
    def execute(self, config: MultiLayersConfig) -> bool:
        # DO NOT OVERRIDE THIS METHOD
        print("Executing step '" + self.id + "'")
        try:
            self._execute(config)
            print("Step '" + self.id + "' executed")
            return True
        except Exception as e:
            print("Step '" + self.id + "' failed")
            print(e)
            self.cancel()
            return False

    # Called when cancelation of the step is requested
    def cancel(self, config: MultiLayersConfig):
        # DO NOT OVERRIDE THIS METHOD
        print("Canceling step '" + self.id + "' and its changes")
        self._cancel()
        print("Step '" + self.id + "' canceled")

    def __str__(self):
        return self.id