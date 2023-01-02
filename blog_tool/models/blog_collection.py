from __future__ import annotations
from typing import List

from blog_tool.models.blog import Blog
from blog_tool.models.metadata.metadata_blog_collection import BlogCollectionMetadata


class BlogCollection:
    def __init__(self, metadata: BlogCollectionMetadata) -> None:
        super().__init__()
        if metadata is None:
            raise ValueError("The metadata is invalid or null")
        self._metadata = metadata

    @property
    def id(self) -> str:
        if not self._metadata:
            raise ValueError("The blog collection meta data is invalid or null")
        return self._metadata.id

    @property
    def name(self) -> str:
        if not self._metadata:
            raise ValueError("The blog collection meta data is invalid or null")
        return self._metadata.name

    @property
    def description(self) -> str:
        if not self._metadata:
            raise ValueError("The blog collection meta data is invalid or null")
        return self._metadata.description

    @property
    def summary(self) -> str:
        if not self._metadata:
            raise ValueError("The blog collection meta data is invalid or null")
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
