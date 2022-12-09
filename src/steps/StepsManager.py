from src.const import Steps, Paths
from typing import Dict
from src.steps.AStep import AStep
import os
import importlib

class StepsManager:

    # Dictionary of steps
    steps = Dict[str, AStep]

    # Load all steps from the steps folder
    @classmethod
    def load_steps(cls):
        # Clear steps dictionary
        cls.steps = {}
        # For all directories in the steps folder
        for step in os.listdir(Paths.STEPS_TYPE_ROOT):
            try:
                # Import step module
                step_module = importlib.import_module(Paths.STEPS_TYPE_ROOT + Paths.IMPORT_SEPARATOR + step)
                # Get step class
                step_class = getattr(step_module, "Step")
                # Verify step is a step
                if not issubclass(step_class, AStep):
                    raise Exception("Step '" + step + "' is not a step")
                # Put step in dictionary
                cls.steps[step] = step_class
            except Exception as e:
                raise Exception("Failed to load step '" + step + "'")

    # Get step from type id
    @classmethod
    def get_step(cls, step_id: str):
        # Verify step exists
        if step_id not in cls.steps.keys():
            return None
        return cls.steps[step_id]