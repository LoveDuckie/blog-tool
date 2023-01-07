from typing import Any
import pydantic
from blog_tool.models.configuration.publisher import PublisherConfig


class PublishersConfig(pydantic.BaseModel):
    publishers: list[PublisherConfig]

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
