import unittest

from blog_tool.utility.paths.utility_paths_blog import get_default_collection_id, get_default_collection_path, get_default_collections_path


class TestPaths(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_default_collections_path(self):
        assert get_default_collections_path() is not None

    def test_default_collection_path(self):
        assert get_default_collection_path(get_default_collection_id()) is not None
