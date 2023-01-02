from abc import ABC, abstractmethod


from blog_tool.models.blog import Blog


class PublisherInterface(ABC):
    def __init__(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    async def publish(self, blog: Blog, **kwargs):
        if blog is None:
            raise ValueError("The blog is invalid or null")
