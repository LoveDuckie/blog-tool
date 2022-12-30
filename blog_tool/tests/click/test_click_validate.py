import os
import unittest
from click.testing import CliRunner

from blog_tool.git.utils import get_git_repo_branch_name, get_git_repo_root


class TestClickValidate(unittest.TestCase):
    def setUp(self):
        self.cli_runner = CliRunner()

    def tearDown(self):
        pass

    def test_git_repo_path(self):
        repo_root_path: str = get_git_repo_root()
        self.assertTrue(repo_root_path != "")
        self.assertTrue(os.path.exists(repo_root_path))

    def test_git_branch(self):
        git_branch_name: str = get_git_repo_branch_name()
        self.assertTrue(git_branch_name != "")
