from dataclasses import dataclass
from typing import ClassVar, Optional

@dataclass
class Highlights:
    page: Optional[int]
    loc: str
    note: Optional[str]
    quote: str

@dataclass
class Pages:
    page_instances: ClassVar[list] = []
    title: str
    author: str
    highlights: list[Highlights]

    def __new__(cls, **kwargs):
        cls.page_instances.append(kwargs['title'])
        instance = super().__new__(cls)
        return instance