"""Custom exceptions for the mod pack creator."""


class ModPackCreatorError(Exception):
    """Base class for exceptions in this module."""
    pass


"""Thick config exceptions."""


class MultiLayersVariablesError(ModPackCreatorError):
    """Base class for exceptions in this module."""

    def __init__(self, actual_level_name):
        super().__init__()
        self.actual_level_name = actual_level_name

    def __str__(self):
        return f"Error in level {self.actual_level_name}."


class MultiLayersVariablesInitError(MultiLayersVariablesError):
    """Exception raised when the init of MultiLayersVariables is not done correctly."""

    def __str__(self):
        return f"Error in level {self.actual_level_name} during the initialization."


class MultiLayersVariablesKeyError(MultiLayersVariablesError):
    """Exception raised when a key is not found in the actual level or in the precedent levels."""

    def __init__(self, actual_level_name, key):
        super().__init__(actual_level_name)
        self.key = key

    def __str__(self):
        return f"Key '{self.key}' not found in level {self.actual_level_name} or in precedent levels."


class MultiLayersVariablesReferenceError(MultiLayersVariablesError):
    """Exception raised when a reference is not found in the precedent levels."""

    def __init__(self, actual_level_name, key, precedent_key):
        super().__init__(actual_level_name)
        self.precedent_key = precedent_key
        self.key = key

    def __str__(self):
        return f"Reference '{self.key}' to key '{self.precedent_key}' not found in precedent levels."


class MultiLayersVariablesNoPrecedentError(MultiLayersVariablesReferenceError):
    """Exception raised when a precedent variables is not defined."""

    def __init__(self, actual_level_name, key, precedent_key):
        super().__init__(actual_level_name, key, precedent_key)

    def __str__(self):
        return f"Reference '{self.key}' to key '{self.precedent_key}' not found in precedent levels because there is no precedent levels."


class RestrictedCharactersError(ModPackCreatorError):
    """Exception raised when a string contains restricted characters."""

    def __init__(self, value, allowed):
        super().__init__()
        self.value = value
        self.allowed = allowed

    def __str__(self):
        return f"String '{self.value}' contains restricted characters. Allowed characters are '{self.allowed}'."


class StepError(ModPackCreatorError):
    """Base class for exceptions in this module."""
    pass


class StepTypesInitError(StepError):
    """Exception raised when an error occurred during the initialization of a step."""
    def __init__(self, step_type):
        super().__init__()
        self.step_type = step_type

    def __str__(self):
        return f"Step type '{self.step_type}' does not exist."


class InvalidStepTypeError(StepError):
    """Exception raised when loading an invalid step."""

    def __init__(self, step_type):
        super().__init__()
        self.step_type = step_type

    def __str__(self):
        return f"'{self.step_type}' is not a step type. It should be a python module containing a class named 'Step' inheriting from 'AStep'."


class StepTypesNotLoadedError(StepError):
    """Exception raised when a step is initialized if the steps are not loaded."""

    def __str__(self):
        return f"Steps are not loaded. You should call 'StepsLoader.load_steps()' before using steps."


class StepTypeDoesNotExistError(StepError):
    """Exception raised when a step type does not exist."""

    def __init__(self, step_type):
        super().__init__()
        self.step_type = step_type

    def __str__(self):
        return f"Step type '{self.step_type}' does not exist."


class StepInitError(StepError):
    """Exception raised when an error occurred during the initialization of a step."""

    def __init__(self, step_type, step_config):
        super().__init__()
        self.step_type = step_type
        self.step_config = step_config
        self.step_name = step_config.id

    def __str__(self):
        return f"Error during the initialization of step '{self.step_name}' of type '{self.step_type}'."


class WorkflowError(ModPackCreatorError):
    """Base class for exceptions in this module."""
    pass


class WorkflowInitError(WorkflowError):
    """Exception raised when an error occurred during the initialization of a workflow."""

    def __init__(self, workflow_id):
        super().__init__()
        self.workflow_id = workflow_id

    def __str__(self):
        return f"Error during the initialization of workflow '{self.workflow_id}'."


class WorkflowPrepareStepsError(WorkflowError):
    """Exception raised when an error occurred during the preparation of the steps of a workflow."""

    def __init__(self, workflow_id):
        super().__init__()
        self.workflow_id = workflow_id

    def __str__(self):
        return f"Error during the preparation of the steps of workflow '{self.workflow_id}'."


class WorkflowExecuteError(WorkflowError):
    """Exception raised when an error occurred during the execution of a workflow."""

    def __init__(self, workflow_id):
        super().__init__()
        self.workflow_id = workflow_id

    def __str__(self):
        return f"Error during the execution of workflow '{self.workflow_id}'."


class WorkflowCancelError(WorkflowError):
    """Exception raised when an error occurred during the cancellation of a workflow."""

    def __init__(self, workflow_id):
        super().__init__()
        self.workflow_id = workflow_id

    def __str__(self):
        return f"Error during the cancellation of workflow '{self.workflow_id}'."


class ProjectError(ModPackCreatorError):
    """Base class for exceptions in this module."""
    pass


class ProjectConfigError(ProjectError):
    """Exception raised when an error occurred during the loading of the project configuration."""

    def __init__(self, project_id):
        super().__init__()
        self.project_id = project_id

    def __str__(self):
        return f"Error during the loading of the project configuration of project '{self.project_id}'."


class ProjectVariablesError(ProjectError):
    """Exception raised when an error occurred during the loading of the project variables."""

    def __init__(self, project_id):
        super().__init__()
        self.project_id = project_id

    def __str__(self):
        return f"Error during the loading of the project variables of project '{self.project_id}'."


class ProjectInitError(ProjectError):
    """Exception raised when an error occurred during the initialization of a project."""

    def __init__(self, project_id):
        super().__init__()
        self.project_id = project_id

    def __str__(self):
        return f"Error during the initialization of project '{self.project_id}'."



