from __future__ import annotations
from typing import List, Optional
import os
from typing import Any, List, Optional
from pydantic import BaseModel


class BlogMetadata(BaseModel):
    id: str  # The ID or identifier
    name: str
    checksum: str
    summary: str
    programming_languages: Optional[List[str]]
    technologies: Optional[List[str]]
    platforms: Optional[List[str]]
    tags: Optional[List[str]]
    path: Optional[str]  # The path to where the blog is located.
    filepath: Optional[str]

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

    @classmethod
    def create(cls, metadata_filepath: str, **kwargs) -> BlogMetadata:
        if metadata_filepath is None:
            raise ValueError(
                "The filepath to the metadata is invalid or null.")

        metadata_path = os.path.dirname(metadata_filepath)
        if not os.path.exists(metadata_path):
            os.makedirs(metadata_path)

        blog_metadata = cls(**kwargs)
        blog_metadata.save(metadata_filepath)
        return blog_metadata

    def save(self, metadata_filepath: str = None):
        metadata_filepath = metadata_filepath if metadata_filepath is not None else self.filepath
        if not metadata_filepath:
            raise ValueError(
                "The metadata file path is invalid or null. Unable to continue.")

    @classmethod
    def load(cls, metadata_filepath: str) -> BlogMetadata:
        """The load the metadata file

        Args:
            metadata_filepath (str): The absolute path to the metadata

        Raises:
            ValueError: If the metadata file path is invalid or null
            IOError: If the metadata file does not exist

        Returns:
            BlogMetadata: The newly deserialized meta data
        """
        if metadata_filepath is None:
            raise ValueError("The metadata is invalid or null")
        if not os.path.exists(metadata_filepath):
            raise IOError(
                f"Failed: the file \"{metadata_filepath}\" is invalid or null")

        file_content = None

        with open(metadata_filepath, "r") as f:
            file_content = f.read()
            if file_content is None:
                raise ValueError("The content of the file is invalid or null")

        metadata = BlogMetadata.parse_raw(
            file_content, content_type='application/json')
        if metadata is None:
            raise ValueError(
                "The loaded metadata is invalid or null. Unable to continue.")
