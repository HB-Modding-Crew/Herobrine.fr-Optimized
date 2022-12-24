from typing import Dict
from src.workflows.Workflow import Workflow
import os
from src.const import Paths

class WorkflowsManager:
    """Class to manage workflows"""

    # Dict of workflows
    _workflows: Dict[str, Workflow] = {}

    # Load all workflows
    @classmethod
    def load_workflows(cls):
        # Clear workflows dictionary
        cls._workflows = {}
        # For all workflows
        for workflow in os.listdir(Paths.WORKFLOW_ROOT):
            # Verify file is a json file
            if not workflow.endswith(".json"):
                continue
            # Load workflow
            cls._workflows[workflow.replace(".json", "")] = Workflow(Paths.WORKFLOW_ROOT + Paths.SEPARATOR + workflow)

    # Get workflow from id
    @classmethod
    def get_workflow(cls, workflow_id: str):
        # Verify workflow exists
        if workflow_id not in cls._workflows.keys():
            return None
        return cls._workflows[workflow_id]

    # Get all workflows
    @classmethod
    def get_workflows(cls):
        return cls._workflows.keys()