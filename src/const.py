import os

# Thick config
class MultiLayersConfig:
    # Regex
    REGEX_REF_PRECEDENT = r"ref:(?P<key>.+)"

# Steps
class Steps:
    # Fields
    FIELD_ID = "id"
    FIELD_CONFIG = "config"

# Paths
class Paths:
    # Separators
    SEPARATOR = os.path.sep
    IMPORT_SEPARATOR = "."

    # Import paths

    # Relative paths
    STEPS_TYPE_ROOT = "steps_types"
    WORKFLOW_ROOT = "workflows"
    DEFAULT_WORKFLOW_ROOT = "default_workflows"
    DEFAULT_STEPS_ROOT = "default_steps_types"

# Workflow
class Workflow:
    # Fields
    FIELD_DESCRIPTION = "description"
    FIELD_STEPS = "steps"
    FIELD_AUTHOR = "author"
    FIELD_VERSION = "version"