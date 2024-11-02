from typing import Any
import pydantic
from blog_tool.models.configuration.publisher import PublisherConfig


class PublishersConfig(pydantic.BaseModel):
    publishers: list[PublisherConfig]

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
