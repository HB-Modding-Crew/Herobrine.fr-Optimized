from src.steps import AStep

# Step class is a step that can be used in a workflow
class Step(AStep.AStep):
    # Constructor
    def __init__(self, id: str, step_config: dict):
        # Call super constructor
        super().__init__(id, step_config)

    # Actions to execute when the step is executed
    def _execute(self):
        print("TestStep execution")

    # Actions to execute when the step is canceled
    def _cancel(self):
        print("TestStep cancelation")