from unittest import TestCase

from src.common.MultiLayersVariables import MultiLayersVariables

from src.exeptions import MultiLayersVariablesKeyError, MultiLayersVariablesReferenceError, MultiLayersVariablesNoPrecedentError, MultiLayersVariablesInitError


class TestMultiLayersVariables(TestCase):

    # Test init method.
    def test__init__(self):
        # Create a MultiLayersVariables instance without precedent variables
        handler = MultiLayersVariables(variables={"test_key": "test_item"}, level_name="test_name")

        # Check if the raw variables is {"test_key": "test_item"}
        self.assertEqual(handler["test_key"], "test_item")

    # Test __setraw method.
    def test__set_raw_variables(self):
        # Create a MultiLayersVariables instance without precedent variables
        handler = MultiLayersVariables(variables={}, level_name="test_name")

        # Set raw variables
        handler._set_raw_variables(variables={"test_key": "test_item"})

        # Check if the raw variables is {"test_key": "test_item"}
        self.assertEqual(handler._MultiLayersVariables__raw_variables, {"test_key": "test_item"})

    # Test __set_precedent method.
    def test__set_precedent_variables(self):
        # Create a MultiLayersVariables instance without precedent variables
        handler = MultiLayersVariables(variables={}, level_name="test_name")

        # Create a precedent MultiLayersVariables instance
        precedent_handler = MultiLayersVariables(variables={}, level_name="precedent_test_name")

        # Set precedent variables
        handler._set_precedent_variables(precedent_variables=precedent_handler)

        # Check if the precedent variables is precedent_handler
        self.assertEqual(handler._MultiLayersVariables__precedent_variables, precedent_handler)

    # Test __set_level_name method.
    def test__set_level_name(self):
        # Create a MultiLayersVariables instance without precedent variables
        handler = MultiLayersVariables(variables={}, level_name="test_name")

        # Set level name
        handler._set_level_name(level_name="new_test_name")

        # Check if the level name is "new_test_name"
        self.assertEqual(handler._MultiLayersVariables__level_name, "new_test_name")

    # Test getitem methode without precedent variables.
    def test__getitem__without_precedent(self):
        # Create a MultiLayersVariables instance without precedent variables
        handler = MultiLayersVariables(variables={"test_key": "test_item"}, level_name="test_name")

        # Check if the item "test_key" is "test_item"
        self.assertEqual(handler["test_key"], "test_item")

    # Test getitem methode with precedent variables.
    def test__getitem__with_precedent(self):
        # Create a precedent MultiLayersVariables instance
        precedent_handler = MultiLayersVariables(variables={"precedent_test_key": "precedent_test_item"}, level_name="precedent_test_name")

        # Create a MultiLayersVariables instance with precedent variables
        handler = MultiLayersVariables(variables={}, level_name="test_name", precedent_variables=precedent_handler)

        # Check if the item "precedent_test_key" is "precedent_test_item"
        self.assertEqual(handler["precedent_test_key"], "precedent_test_item")

    # Test getitem method with precedent variables and reference.
    def test__getitem__with_precedent_and_reference(self):
        # Create a precedent MultiLayersVariables instance
        precedent_handler = MultiLayersVariables(variables={"precedent_test_key": "precedent_test_item"}, level_name="precedent_test_name")

        # Create a MultiLayersVariables instance with precedent variables
        handler = MultiLayersVariables(variables={"test_key": "ref:precedent_test_key"}, level_name="test_name", precedent_variables=precedent_handler)

        # Check if the item "test_key" is "precedent_test_item"
        self.assertEqual(handler["test_key"], "precedent_test_item")

    # Test getitem method exeption without precedent variables.
    def test__getitem__without_precedent_exception(self):
        # Create a MultiLayersVariables instance without precedent variables
        handler = MultiLayersVariables(variables={"test_key": "test_item", "ref_item": "ref:invalid_ref"}, level_name="test_name")

        # Try to get an inexistent item
        with self.assertRaises(MultiLayersVariablesKeyError):
            handler["invalid_key"]

        # Try to get an item with an invalid reference
        with self.assertRaises(MultiLayersVariablesNoPrecedentError):
            handler["ref_item"]

    # Test getitem method exeption with precedent variables.
    def test__getitem__with_precedent_exception(self):
        # Create a precedent MultiLayersVariables instance
        precedent_handler = MultiLayersVariables(variables={"precedent_test_key": "precedent_test_item"}, level_name="precedent_test_name")

        # Create a MultiLayersVariables instance with precedent variables
        handler = MultiLayersVariables(variables={"test_key": "ref:invalid_ref"}, level_name="test_name", precedent_variables=precedent_handler)

        # Try to get an invalid item
        with self.assertRaises(MultiLayersVariablesKeyError):
            handler["MultiLayersVariablesKeyError"]

        # Try to get an item with an invalid reference
        with self.assertRaises(MultiLayersVariablesReferenceError):
            handler["test_key"]

    # Test initialization exception.
    def test__init__exception(self):
        # Try to create a MultiLayersVariables instance with invalid precedent variables
        with self.assertRaises(MultiLayersVariablesInitError):
            MultiLayersVariables(variables={}, level_name="test_name", precedent_variables="precedent_handler")

        # Try to create a MultiLayersVariables instance with invalid level name
        with self.assertRaises(MultiLayersVariablesInitError):
            MultiLayersVariables(variables={}, level_name=1)

        # Try to create a MultiLayersVariables instance with invalid raw variables
        with self.assertRaises(MultiLayersVariablesInitError):
            MultiLayersVariables(variables=1, level_name="test_name")

        # Try to create a MultiLayersVariables instance with characters not allowed in level name
        with self.assertRaises(MultiLayersVariablesInitError):
            MultiLayersVariables(variables={}, level_name="test_name$")


