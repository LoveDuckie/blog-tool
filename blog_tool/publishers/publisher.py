from blog_tool.errors.blog_tool_exception import BlogToolException
from blog_tool.models.blog import Blog
from blog_tool.publishers.publisher_interface import PublisherInterface


class Publisher:
    def __init__(self, *args, **kwargs) -> None:
        pass

    async def upload(self, publisher_interface: PublisherInterface, blog: Blog):
        if not publisher_interface:
            raise ValueError("The publisher interface specified is invalid or null")
        if not isinstance(publisher_interface, PublisherInterface):
            raise TypeError("  ")
        if not blog:
            raise ValueError("The blog instance is invalid or null")
        try:
            publisher_interface.publish(blog)
        except BlogToolException as exc:
            pass
