import json
from src.common.MultiLayersConfig import MultiLayersConfig

class Project:
    """A class handling project informations."""

    # Init with project.json
    def __init__(self, project_json: dict):
        self._project_json = project_json

        # Open project.json
        with open(project_json, "r") as f:
            self._project = json.load(f)
            # Get project name
            self.name = self._project["name"]
            # Get project version
            self.version = self._project["version"]
            # Get project author
            self.author = self._project["author"]
            # Get project workflows list
            self.workflows = self._project["workflows"]
            # Get project variables
            self.variables = self._project["variables"]
        
        # Set config as a MultiLayersConfig
        self.set_config(self.variables)

    # Set _config as a MultiLayersConfig
    def set_config(self, config: dict):
        self._config = MultiLayersConfig(config, "Project Variables", self.variables)
            