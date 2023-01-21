from __future__ import annotations
import json
import os

from blog_tool.models.metadata.metadata_blog import BlogMetadata
from blog_tool.utility.paths.utility_paths_blog import get_default_blog_metadata_filename


class Blog:
    def __init__(self, metadata: BlogMetadata) -> None:
        self._collection = None
        self._content = None
        self._description = None
        self._id = None
        self._name = None
        if metadata is None:
            raise ValueError("The metadata for this blog is invalid or null")
        self._metadata = metadata
        self._loaded = False
        super().__init__()

    @property
    def metadata(self):
        return self._metadata

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @property
    def content(self):
        if self._loaded and hasattr(self, "_content"):
            return self._content

        return self._content

    @property
    def collection(self):
        return self._collection

    @classmethod
    def load_blog(cls, blog_path):  # sourcery skip: raise-specific-error
        if blog_path is None or blog_path == '':
            raise ValueError("The blog path is invalid or null")

        if not os.path.isabs(blog_path):
            raise IOError(
                f'The path \"{blog_path}\" is not an absolute path. Unable to continue.')

        if not os.path.isdir(blog_path):
            raise IOError(
                f'The path \"{blog_path}\" is not a valid directory. It must be a directory.')

        blog_metadata_filepath = os.path.join(blog_path, get_default_blog_metadata_filename())

        if not os.path.isfile(blog_metadata_filepath):
            raise IOError(
                f'The file \"{blog_metadata_filepath}\" is not a valid file')

        if not os.path.exists(blog_metadata_filepath):
            raise Exception(
                f'Unable to find the metadata file \"{blog_metadata_filepath}\".')

        blog_metadata = None

        with open(blog_metadata_filepath, 'r') as file:
            blog_metadata = file.read()
            if blog_metadata is None:
                raise ValueError("The blog metadata is invalid or null")

        if blog_metadata is None:
            raise ValueError("The loaded metadata is invalid or null")

        loaded_metadata = json.loads(blog_metadata)

        if loaded_metadata is None:
            raise ValueError("The loaded metadata is invalid or null")

        if not isinstance(loaded_metadata, dict):
            raise TypeError('The loaded metadata was not a dictionary.')

        return cls(**loaded_metadata)
