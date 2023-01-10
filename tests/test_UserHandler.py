from unittest import TestCase

from src.User.UserHandler import UserHandler


class TestUserHandler(TestCase):

    def test_init(self):
        # Test the init
        user_handler = UserHandler()
