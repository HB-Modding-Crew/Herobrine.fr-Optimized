from dacite import from_dict
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class StepData:
    """A class handling step data."""
    id: str
    type: str
    config: Dict[str, Any]

@dataclass
class WorkflowData:
    """A class handling workflow data."""
    name: str
    version: str
    author: str
    steps: List[StepData]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return from_dict(cls, data)