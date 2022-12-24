import json
from src.common.MultiLayersConfig import MultiLayersConfig
import os
from src.projects.ProjectData import ProjectData

class Project:
    """A class handling project informations."""

    # Init with project.json
    def __init__(self, project_json: dict):
        self._project_json = project_json

        # Open project.json
        with open(project_json, "r") as f:
            self._project = json.load(f)
            # Id is the file name
            self.id: str = os.path.basename(project_json).replace(".json", "")
            # Validate project data
            self._data = ProjectData.from_dict(self._project)
        
        # Set config as a MultiLayersConfig
        self.set_config(self._variables)

    @property
    def version(self):
        return self._data.version

    @property
    def author(self):
        return self._data.author
    
    @property
    def name(self):
        return self._data.name

    @property
    def workflows(self):
        return self._data.workflows

    @property
    def _variables(self):
        return self._data.variables

    # Set _config as a MultiLayersConfig
    def set_config(self, config: dict):
        self.variables = MultiLayersConfig(config, "Project Variables")
            