from typing import Dict, Type, Union

from src.Step.AStep import AStep
from src.const import Paths, Indents

import importlib

import os

from src.common.OutputWrapper import OutputWrapper

from src.exeptions import InvalidStepTypeError, StepTypesInitError, StepTypesNotLoadedError, StepTypeDoesNotExistError


class StepTypesManager:

    # Steps type path
    __step_type_path: str = Paths.STEP_TYPES_ROOT
    steps_types: Union[Dict[str, Type[AStep]], None] = None
    __output: OutputWrapper = OutputWrapper(Indents.STEP_TYPE_LEVEL)

    # Load all steps types
    @classmethod
    def load_steps_types(cls) -> bool:
        # Clear steps dictionary
        cls.steps_types = {}
        # For all directories in the steps folder
        for step_type in os.listdir(cls.__step_type_path):
            try:
                # Verify is directory
                if not os.path.isdir(cls.__step_type_path + Paths.SEPARATOR + step_type):
                    continue
                # Import step module
                step_type_module = importlib.import_module(cls.__step_type_path + Paths.IMPORT_SEPARATOR + step_type)
                # Get step class
                step_type_class = getattr(step_type_module, "Step")
                # Verify step is a step
                if not issubclass(step_type_class, AStep):
                    raise InvalidStepTypeError(step_type)
                # Put step in dictionary
                cls.steps_types[step_type] = step_type_class
                # Log step type loaded
                cls.__output.fill("Step type '" + step_type + "' loaded")
            except Exception as e:
                # Output error
                cls.__output.fill(str(e))
                cls.__output.fill("Failed to load step type '" + step_type + "'")
                raise StepTypesInitError(step_type) from e
        return True

    # Set steps path (for tests)
    @classmethod
    def set_steps_path(cls, path: str):
        cls.__step_type_path = path

    # For tests only
    @classmethod
    def reset(cls):
        cls.steps_types = None

    @classmethod
    def get_step_type(cls, step_type_id: str) -> Type[AStep]:
        # Verify steps are loaded
        if not cls._is_initialized():
            raise StepTypesNotLoadedError()
        # Verify step exists
        if step_type_id not in cls.steps_types.keys():
            raise StepTypeDoesNotExistError(step_type_id)
        return cls.steps_types[step_type_id]

    @classmethod
    def _is_initialized(cls) -> bool:
        return cls.steps_types is not None



