from unittest import TestCase
from module1.main import get_message


class Module1TestCase(TestCase):
    def test_msg_write(self):
        self.assertEqual(get_message("Hello World!"), "Hello World!")
