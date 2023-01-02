from typing import Any
import pydantic


class PublishersConfig(pydantic.BaseModel):
    publishers: list[PublisherConfig]
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
