import json
from src.const import Workflow as ConstWorkflow, Paths, Steps
from src.steps_types.AStep import AStep
from src.steps_types.StepsTypesManager import StepsTypesManager
from src.common.InputConfirmation import confirm_yes_or_no
import os
from src.workflows.WorkflowData import WorkflowData, StepData
from typing import List

# Workflow class
# Can be instantiated with a workflow json file
# A workflow is a list of steps
class Workflow:
    """A class representing workflows."""
    # Constructor
    def __init__(self, workflow_file: str):
        # Open workflow file
        with open(workflow_file) as json_file:
            # Load workflow file
            self.workflow = json.load(json_file)
            # Workflow id is the file name
            self.id = os.path.basename(workflow_file).replace(".json", "")
            # Validate workflow data
            self._data = WorkflowData.from_dict(self.workflow)
            # Get steps datas
            self._steps = self._data.steps
            # List of steps
            self.steps: List[AStep] = []
        for step in self._steps:
            # Get step class from step id
            step_class = StepsTypesManager.get_step_type(step.id)
            # If not found, raise exception
            if step_class is None:
                raise Exception("Step type '" + step.id + "' not found")
            # Instantiate step
            self.steps.append(step_class(step.id, step.config))

    @property
    def version(self):
        return self._data.version

    @property
    def author(self):
        return self._data.author
    
    @property
    def name(self):
        return self._data.name

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
