from src.Step.AStep import AStep
from src.exeptions import MultiLayersVariablesNoPrecedentError, MultiLayersVariablesReferenceError
from src.Workflow.WorkflowVariables import WorkflowVariables
from src.Step.StepConfig import StepConfig


# Step class is a step that can be used in a workflow
class Step(AStep):
    # Constructor
    def __init__(self, step_config: StepConfig, workflow_variables: WorkflowVariables):
        # Call super constructor
        super().__init__(step_config, workflow_variables)

    # Actions to execute when the step is executed
    def _execute(self) -> bool:
        self.log("TestStep execution")
        return True

    # Actions to execute when the step is canceled
    def _cancel(self):
        self.log("TestStep cancellation")
