from typing import Any
import pydantic


class PublisherConfig(pydantic.BaseModel):
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
