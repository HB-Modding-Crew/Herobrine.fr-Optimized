from unittest import TestCase
from src.Step.StepTypesManager import StepTypesManager
from src.Step.AStep import AStep

from typing import Any

from src.exeptions import StepsNotLoadedError, StepTypeDoesNotExistError, StepInitError


class TestStepsTypesManager(TestCase):

    def test_load_steps_types(self):
        # Change steps path for tests
        StepTypesManager.set_steps_path("example_steps")

        # Load steps types
        self.assertTrue(StepTypesManager.load_steps_types())

    # Test get step type
    def test_get_step_type(self):
        # Change steps path for tests
        StepTypesManager.set_steps_path("example_steps")

        # Load steps types
        StepTypesManager.load_steps_types()

        # Get step type
        step_type: Any = StepTypesManager.get_step_type("teststep")

        # Verify step type is not None
        self.assertIsNotNone(step_type)

        # Verify step type is a step
        self.assertTrue(issubclass(step_type, AStep))

    # Tests errors
    def test_errors(self):
        # Be sure steps types are not loaded
        StepTypesManager.reset()

        # Set steps path for tests
        StepTypesManager.set_steps_path("example_steps")

        # Try to get step type
        with self.assertRaises(StepsNotLoadedError):
            StepTypesManager.get_step_type("teststep")

        # Load steps types
        StepTypesManager.load_steps_types()

        # Try to get step type that does not exist
        with self.assertRaises(StepTypeDoesNotExistError):
            StepTypesManager.get_step_type("teststep2")

    def test_errors_init(self):
        # Change steps path for tests
        StepTypesManager.set_steps_path("example_steps_invalid")

        # Try to load steps types
        with self.assertRaises(StepInitError):
            StepTypesManager.load_steps_types()
