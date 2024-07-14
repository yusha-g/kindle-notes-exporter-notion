from dataclasses import dataclass
from typing import Optional

@dataclass
class Highlights:
    page: Optional[int]
    loc: str
    note: Optional[str]
    quote: str

@dataclass
class Pages:
    title: str
    author: str
    highlights: list[Highlights]