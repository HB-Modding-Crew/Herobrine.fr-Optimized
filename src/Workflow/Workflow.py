from src.Project.ProjectVariables import ProjectVariables

from src.Workflow.WorkflowVariables import WorkflowVariables
from src.Workflow.WorkflowConfig import WorkflowConfig

from src.const import Step as WorkflowConsts, Indents

from src.common.OutputWrapper import OutputWrapper

class Workflow:

    output_wrapper_workflow: OutputWrapper = OutputWrapper(ident_size=Indents.WORKFLOW_LEVEL)
    __workflow_variables: WorkflowVariables = None
    __initialized: bool = False