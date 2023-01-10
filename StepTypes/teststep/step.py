from src.Step.AStep import AStep


class Step(AStep):

    def _execute(self) -> bool:
        # Execute step log
        self.output_wrapper_step.fill("Inside step execute")

        # Return true
        return True

    def _cancel(self):
        # Cancel step log
        self.output_wrapper_step.fill("Inside step cancel")

        # Return true
        return True


