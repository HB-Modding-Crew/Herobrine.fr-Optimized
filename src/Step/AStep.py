from src.Workflow.WorkflowVariables import WorkflowVariables

from src.Step.StepConfig import StepConfig
from src.Step.StepVariables import StepVariables

from src.common.OutputWrapper import OutputWrapper

from src.const import Step as StepConsts, Indents

from src.exeptions import StepsNotLoadedError


# Must not be instantiated
# Abstract class
class AStep:

    __output_wrapper_system: OutputWrapper = OutputWrapper(ident_size=Indents.STEP_LEVEL_SYSTEM)
    output_wrapper_step: OutputWrapper = OutputWrapper(ident_size=Indents.STEP_LEVEL_STEP)
    __step_variables: StepVariables = None
    __initialized: bool = False

    def __int__(self):
        pass

    def __init(self, step_config: StepConfig, workflow_variables: WorkflowVariables) -> bool:
        # Init step variables
        try:
            # Init step log
            print(self.__output_wrapper_system.fill(StepConsts.INIT_STEP_FORMAT.format(step_name=step_config.name)))

            # Verify type
            if not isinstance(step_config, StepConfig):
                raise TypeError("Step config must be a StepConfig")
            if not isinstance(workflow_variables, WorkflowVariables):
                raise TypeError("Workflow variables must be a WorkflowVariables")
            # Create step self.__step_variables
            self.__step_variables = StepVariables(step_config=step_config, workflow_variables=workflow_variables)

            # End init step log
            print(
                self.__output_wrapper_system.fill(StepConsts.INIT_STEP_DONE_FORMAT.format(step_name=step_config.name)))
            # Return True
            return True
        except Exception as e:
            # Exception log
            print(self.__output_wrapper_system.fill(str(e)))
            # Failed init step log
            print(self.__output_wrapper_system.fill(
                StepConsts.INIT_STEP_FAILED_FORMAT.format(step_name=step_config.name)))
            # Return False
            return False

    def execute(self) -> bool:
        """
        Step execution wrapper. Call the overridable method _execute
        May be overriden in a child abstract step class
        Should not be overriden in a final step type class

        :return:
        """

        # Verify if not initialized
        if not self.__initialized:
            raise StepsNotLoadedError()

        # Execute step
        try:
            # Execute step log
            print(self.__output_wrapper_system.fill(StepConsts.EXECUTION_STEP_FORMAT.format(step_name=self.__step_variables.step_name)))

            # Execute step
            res = self._execute()

            # Verify result
            # If true
            if res:
                # End execute step log
                print(self.__output_wrapper_system.fill(StepConsts.EXECUTION_STEP_DONE_FORMAT.format(step_name=self.__step_variables.step_name)))
            # If false
            print(self.__output_wrapper_system.fill(StepConsts.EXECUTION_STEP_FAILED_FORMAT.format(step_name=self.__step_variables.step_name)))
            return res
        except Exception as e:
            # Exception log
            print(self.__output_wrapper_system.fill(str(e)))
            # Failed execute step log
            print(self.__output_wrapper_system.fill(StepConsts.EXECUTION_STEP_FAILED_FORMAT.format(step_name=self.__step_variables.step_name)))
            # Return False
            return False

    def _execute(self) -> bool:
        """
        Step execution.
        Must be overriden in a final step type class
        :return:
        """
        raise NotImplementedError("_execute method must be overriden in a final step type class")

    def cancel(self):
        """
        Step cancellation.
        May be overriden in a child abstract step class
        Should not be overriden in a final step type class

        Should be able to cancel the step even if the step has failed at any time
        Should never fail (try all cancellations possible)
        :return:
        """
        # Verify if not initialized
        if not self.__initialized:
            raise StepsNotLoadedError()

        # Cancel step
        try:
            # Cancel step log
            print(self.__output_wrapper_system.fill(StepConsts.CANCEL_STEP_FORMAT.format(step_name=self.__step_variables.step_name)))

            # Cancel step
            self._cancel()

            # End cancel step log
            print(self.__output_wrapper_system.fill(StepConsts.CANCEL_STEP_DONE_FORMAT.format(step_name=self.__step_variables.step_name)))

        except Exception as e:
            # Exception log
            print(self.__output_wrapper_system.fill(str(e)))
            # Failed cancel step log
            print(self.__output_wrapper_system.fill(StepConsts.CANCEL_STEP_FAILED_FORMAT.format(step_name=self.__step_variables.step_name)))

    def _cancel(self):
        """
        Step cancellation.
        Must be overriden in a final step type class
        :return:
        """
        raise NotImplementedError("_cancel method must be overriden in a final step type class")

    def log(self, message: str):
        """
        Log a message in the step log
        :param message:
        :return:
        """
        print(self.output_wrapper_step.fill(message))
