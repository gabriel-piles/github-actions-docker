from typing import List

from pydantic import BaseModel


class Data(BaseModel):
    paragraphs: List[str]
