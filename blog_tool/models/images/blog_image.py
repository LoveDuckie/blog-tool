from typing import Any
import pydantic


class BlogImage(pydantic.BaseModel):
    path: str
    checksum: str

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
