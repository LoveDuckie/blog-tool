from __future__ import annotations
import json
import os
from typing import Any, List, Optional
from pydantic import BaseModel

from blog_tool.models.blog import Blog
from blog_tool.utility.click.utility_click import click_write_error, click_write_info


class BlogCollectionMetadata(BaseModel):
    id: str
    name: str
    description: Optional[str]
    summary: Optional[str]
    metadata: dict[str, dict]
    path: Optional[str]
    filepath: Optional[str]
    tags: Optional[List[str]]

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

    def get_collection_path(self) -> str:
        pass

    def get_blog_path(self, blog_id: str) -> str:
        if not blog_id:
            raise ValueError
        return

    @classmethod
    def create(cls, metadata_filepath: str, **kwargs) -> BlogCollectionMetadata:
        if metadata_filepath is None:
            raise ValueError("The metadata file path is invalid or null")

        metadata_path = os.path.dirname(metadata_filepath)
        if not os.path.exists(metadata_path):
            os.makedirs(metadata_path)

        collection_metadata = cls(**kwargs)
        collection_metadata.save(metadata_filepath)

    @classmethod
    def load(cls, metadata_filepath: str, quiet: bool = False) -> BlogCollectionMetadata:
        if metadata_filepath is None:
            raise ValueError("The metadata filepath was not correctly defined")

        if not os.path.abspath(metadata_filepath):
            raise IOError(
                f"Thet path \"{metadata_filepath}\" is not an absolute filepath.")

        if not os.path.exists(metadata_filepath):
            raise IOError(
                f"The absolute path to the metadata is invalid or null (\"{metadata_filepath}\")")

        click_write_info(f"Loading: \"{metadata_filepath}\"")

        with open(metadata_filepath, 'r') as f:
            metadata_raw = f.read()

        if not metadata_raw or metadata_raw == "":
            errmsg = f"The metadata file \"{metadata_filepath}\" is empty."
            click_write_error(errmsg)
            raise IOError(errmsg)

        collection_metadata = BlogCollectionMetadata.parse_raw(metadata_raw)
        collection_metadata.filepath = metadata_filepath
        collection_metadata.path = os.path.dirname(
            os.path.dirname(metadata_filepath))
        return collection_metadata

    def save(self, filepath: str = None):
        if filepath is None and hasattr(self, "filepath"):
            filepath = self.filepath

        content = json.dumps(self)
        if not content:
            raise ValueError("The content is invalid or null")
        with open(filepath, 'w') as f:
            f.write(content)
