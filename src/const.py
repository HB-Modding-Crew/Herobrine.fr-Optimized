from enum import Enum

# Thick config


class MultiLayersVariables:
    # Regex
    REGEX_REF_PRECEDENT = r"ref:(?P<key>.+)"


class Indents(Enum):
    COMMAND_LEVEL = 0
    STEP_TYPE_LEVEL = 1
    WORKFLOW_LEVEL = 1
    STEP_LEVEL_SYSTEM = 2
    STEP_LEVEL_STEP = 3


class Paths:
    # Path components
    SEPARATOR = "/"
    WILDCARD = "*"
    IMPORT_SEPARATOR = "."

    # Project paths
    STEP_TYPES_ROOT = "StepTypes"


class Step:
    """Step types class.
    """

    # Outputs formats
    INIT_STEP_FORMAT = "Initializing step '{step_name}'"
    INIT_STEP_DONE_FORMAT = "Step '{step_name}' initialized"
    INIT_STEP_FAILED_FORMAT = "Step '{step_name}' initialization failed"
    EXECUTION_STEP_FORMAT = "Executing step '{step_name}'"
    EXECUTION_STEP_DONE_FORMAT = "Step '{step_name}' executed"
    EXECUTION_STEP_FAILED_FORMAT = "Step '{step_name}' execution failed"
    CANCEL_STEP_FORMAT = "Cancelling step '{step_name}'"
    CANCEL_STEP_DONE_FORMAT = "Step '{step_name}' cancelled"
    CANCEL_STEP_FAILED_FORMAT = "Step '{step_name}' cancellation failed"
