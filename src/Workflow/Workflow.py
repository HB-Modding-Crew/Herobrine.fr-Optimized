from typing import List, NamedTuple, Type

from src.Step.AStep import AStep
from src.Step.StepConfig import StepConfig

from src.Step.StepTypesManager import StepTypesManager

from src.Project.ProjectVariables import ProjectVariables

from src.Workflow.WorkflowVariables import WorkflowVariables
from src.Workflow.WorkflowConfig import WorkflowConfig

from src.const import Workflow as WorkflowConsts, Indents

from src.common.OutputWrapper import OutputWrapper

from src.exeptions import WorkflowInitError, WorkflowPrepareStepsError, WorkflowCancelError, WorkflowExecuteError


class StepTypeConfigTuple(NamedTuple):
    """
    A tuple containing the Type[AStep] and the step config
    """
    step_type: Type[AStep]
    step_config: StepConfig


class Workflow:

    output_wrapper_workflow: OutputWrapper = OutputWrapper(indent_size=Indents.WORKFLOW_LEVEL)
    __workflow_variables: WorkflowVariables = None
    __initialized: bool = False
    # Steps is a list of named tuples containing the step type and the step config
    steps: List[StepTypeConfigTuple] = []
    executed_steps: List[StepTypeConfigTuple] = []

    def __init__(self, workflow_id: str, workflow_config: WorkflowConfig, project_variables: ProjectVariables):
        """
        Workflow initialization
        :param workflow_id:
        :param workflow_config:
        :param project_variables:
        """
        # Init workflow variables
        try:
            # Init workflow log
            print(self.output_wrapper_workflow.fill(WorkflowConsts.INIT_WORKFLOW_FORMAT.format(workflow_name=workflow_config.name)))

            # Verify type
            if not isinstance(workflow_config, WorkflowConfig):
                raise TypeError("Workflow config must be a WorkflowConfig")
            if not isinstance(project_variables, ProjectVariables):
                raise TypeError("Project variables must be a ProjectVariables")
            # Create workflow variables
            self.__workflow_variables = WorkflowVariables(workflow_id=workflow_id, workflow_config=workflow_config, project_variables=project_variables)
            # Prepare steps
            self.__prepare_steps()
            # End init workflow log
            print(self.output_wrapper_workflow.fill(WorkflowConsts.INIT_WORKFLOW_DONE_FORMAT.format(workflow_name=workflow_config.name)))
        except Exception as e:
            # Raise exception
            raise WorkflowInitError(workflow_id) from e

    def __prepare_steps(self):
        """
        Prepare the steps list
        :return:
        """
        # Prepare steps
        try:
            # Prepare steps log
            print(self.output_wrapper_workflow.fill(WorkflowConsts.PREPARE_STEPS_FORMAT.format(workflow_name=self.__workflow_variables.workflow_name)))

            # Prepare steps
            for step_config in self.__workflow_variables.workflow_steps:
                # Get step type
                step_type = StepTypesManager.get_step_type(step_config.type)
                # Add step to steps list
                self.steps.append(StepTypeConfigTuple(step_type=step_type, step_config=step_config))

            # End prepare steps log
            print(self.output_wrapper_workflow.fill(WorkflowConsts.PREPARE_STEPS_DONE_FORMAT.format(workflow_name=self.__workflow_variables.workflow_name)))
        except Exception as e:
            # Raise exception
            raise WorkflowPrepareStepsError(self.__workflow_variables.id) from e

    def __init_step_for_execution(self, step_type_config_tuple: StepTypeConfigTuple) -> AStep:
        """
        Init a step for execution
        :param step_type_config_tuple:
        :return:
        """
        # Init step
        return step_type_config_tuple.step_type(step_config=step_type_config_tuple.step_config, workflow_variables=self.__workflow_variables)

    def execute(self):
        """
        Execute the workflow
        :return:
        """
        try:
            # Execute workflow log
            print(self.output_wrapper_workflow.fill(WorkflowConsts.EXECUTE_WORKFLOW_FORMAT.format(workflow_name=self.__workflow_variables.workflow_name)))

            # Execute steps
            for step in self.steps:
                # Init step
                instantiated_step = self.__init_step_for_execution(step_type_config_tuple=step)
                # Add step to executed steps
                self.executed_steps.append(step)
                # Execute step
                res = instantiated_step.execute()
                # Check if step failed
                if not res:
                    # Raise exception
                    raise WorkflowExecuteError(self.__workflow_variables.id)

            # End execute workflow log
            print(self.output_wrapper_workflow.fill(WorkflowConsts.EXECUTE_WORKFLOW_DONE_FORMAT.format(workflow_name=self.__workflow_variables.workflow_name)))
        except Exception as e:
            # Raise exception
            raise WorkflowExecuteError(self.__workflow_variables.id) from e

    def cancel(self):
        """
        Cancel the workflow
        :return:
        """
        try:
            # Cancel workflow log
            print(self.output_wrapper_workflow.fill(WorkflowConsts.CANCEL_WORKFLOW_FORMAT.format(workflow_name=self.__workflow_variables.workflow_name)))

            # Cancel steps
            for step in self.executed_steps:
                # Init step
                instantiated_step = self.__init_step_for_execution(step_type_config_tuple=step)
                # Cancel step
                instantiated_step.cancel()

            # End cancel workflow log
            print(self.output_wrapper_workflow.fill(WorkflowConsts.CANCEL_WORKFLOW_DONE_FORMAT.format(workflow_name=self.__workflow_variables.workflow_name)))
        except Exception as e:
            # Raise exception
            raise WorkflowCancelError(self.__workflow_variables.id) from e




