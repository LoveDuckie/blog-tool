from typing import Any
import pydantic

from blog_tool.models.configuration.publisher.config_publishers import PublishersConfig


class RepositoryConfig(pydantic.BaseModel):
    profiles: PublishersConfig

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
