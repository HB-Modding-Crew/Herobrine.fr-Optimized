import json
from src.const import Workflow as ConstWorkflow, Paths, Steps
from src.steps.AStep import AStep
from src.steps.StepsManager import StepsManager
from src.common.InputConfirmation import confirm_yes_or_no
import os

# Workflow class
# Can be instantiated with a workflow json file
# A workflow is a list of steps
class Workflow:
    # Constructor
    def __init__(self, workflow_file: str):
        # Open workflow file
        with open(workflow_file) as json_file:
            # Load workflow file
            self.workflow = json.load(json_file)
            # Workflow id is the file name
            self.id = os.path.basename(workflow_file).replace(".json", "")
            # Get workflow description
            self.description = self.workflow[ConstWorkflow.FIELD_DESCRIPTION]
            # Get workflow steps
            self._steps = self.workflow[ConstWorkflow.FIELD_STEPS]
            self.steps = []
            # Get workflow author
            self.author = self.workflow[ConstWorkflow.FIELD_AUTHOR]
            # Get workflow version
            self.version = self.workflow[ConstWorkflow.FIELD_VERSION]
        for step in self._steps:
            # Get step class from step id
            step_class = StepsManager.get_step(step[Steps.FIELD_ID])
            # If not found, raise exception
            if step_class is None:
                raise Exception("Step type '" + step[Steps.FIELD_ID] + "' not found")
            # Instantiate step
            self.steps.append(step_class(step[Steps.FIELD_ID], step[Steps.FIELD_CONFIG]))

    # Execute workflow
    def execute(self):
        # Succefully executed steps
        executed_steps = []
        # Step type
        step: AStep
        # Log workflow execution
        print("Executing workflow '" + self.id + "'")
        # Execute steps
        for step in self.steps:
            res = step.execute()
            if res:
                executed_steps.append(step)
                continue
            # Ask user if he wants to cancel all the previous steps
            if not confirm_yes_or_no("Do you want to cancel all the previously executed steps ?"):
                print("Previous steps will not be canceled")
                break
            # If yes, cancel all the previously executed steps
            for step in executed_steps:
                step.cancel()
        # Log workflow execution end
        print("Workflow '" + self.id + "' execution ended")
