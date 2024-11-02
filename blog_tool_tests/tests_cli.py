import os
import unittest
from unittest.mock import Mock

from blog_tool.__main__ import cli


class TestCli(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ctx = Mock()
        cls.ctx.obj = {}

    def test_cli_validation(self):
        with self.assertRaises(ValueError):
            cli(self.ctx, "", True, "path/to/config", False)
        with self.assertRaises(IOError):
            cli(self.ctx, "not/absolute/path", True, "path/to/config", False)
        with self.assertRaises(IOError):
            cli(self.ctx, "/non/existent/path", True, "path/to/config", False)
        with self.assertRaises(ValueError):
            cli(self.ctx, os.getcwd(), True, "", False)
        with self.assertRaises(IOError):
            cli(self.ctx, os.getcwd(), True, "not/absolute/path", False)
        with self.assertRaises(IOError):
            cli(self.ctx, os.getcwd(), True, "/non/existent/path", False)

    def test_cli_functionality(self):
        cli(self.ctx, os.getcwd(), True, os.getcwd(), False)
        self.assertEqual(self.ctx.obj['storage_path'], os.getcwd())
        self.assertEqual(self.ctx.obj['config_filepath'], os.getcwd())

    def test_cli_storage_path_creation(self):
        non_existent_path = "/non/existent/path"
        with self.assertRaises(IOError):
            cli(self.ctx, non_existent_path, True, os.getcwd(), False)
        try:
            os.makedirs(non_existent_path)
            cli(self.ctx, non_existent_path, True, os.getcwd(), True)
            self.assertEqual(self.ctx.obj['storage_path'], non_existent_path)
        finally:
            if os.path.exists(non_existent_path):
                os.rmdir(non_existent_path)


if __name__ == "__main__":
    unittest.main()
