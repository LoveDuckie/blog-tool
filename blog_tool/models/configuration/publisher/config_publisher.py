from typing import Any
import pydantic


class PublisherConfig(pydantic.BaseModel):
    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
