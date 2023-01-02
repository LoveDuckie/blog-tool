from blog_tool.publishers.publisher_interface import PublisherInterface

import rich_click as click


class DevToPublisher(PublisherInterface):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def publish(self, content: str):
        if not content:
            raise ValueError("The content is invalid or null")
        return super().publish(content)
