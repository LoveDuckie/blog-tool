from blog_tool.models.blog import Blog
from blog_tool.publishers.publisher_interface import PublisherInterface

import rich_click as click


class DevToPublisher(PublisherInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def publish(self, blog: Blog, **kwargs):
        if not blog:
            raise ValueError("The content is invalid or null")
        return super().publish(blog)
