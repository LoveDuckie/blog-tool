from __future__ import annotations
import json
import os
from typing import Any, List, Optional
from pydantic import BaseModel

from blog_tool.models.blog import Blog
from blog_tool.models.metadata.metadata_blog_collection import BlogCollectionMetadata
from blog_tool.utility.click.utility_click import click_write_error, click_write_info


class BlogCollection:
    def __init__(self, metadata: BlogCollectionMetadata) -> None:
        super().__init__()
        if metadata is None:
            raise ValueError("The metadata is invalid or null")
        self._metadata = metadata

    @property
    def id(self) -> str:
        return self._metadata.id

    @property
    def name(self) -> str:
        return self._metadata.name

    @property
    def description(self) -> str:
        return self._metadata.description

    @property
    def summary(self) -> str:
        return self._metadata.summary

    @property
    def blogs(self) -> List[Blog]:
        if hasattr(self, "blogs"):
            return self.blogs
        blogs = []

        setattr(self, "blogs", blogs)
        return blogs

    def _load_blogs(self):
        return
