from dacite import from_dict
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class ProjectData:
    """A class handling project data."""
    name: str
    version: str
    author: str
    workflows: List[str]
    variables: Dict[str, Any]

    @classmethod
    def from_dict(cls, d: dict):
        return from_dict(data_class=cls, data=d)