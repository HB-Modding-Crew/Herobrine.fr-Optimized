from typing import Dict
from src.projects.Project import Project
import os
from src.const import Paths

class ProjectsManager:
    """Manages the projects"""

    # Dict of projects
    _projects: Dict[str, Project] = {}

    # Load all projects
    @classmethod
    def load_projects(cls):
        # Clear projects dictionary
        cls._projects = {}
        # For all projects
        for project in os.listdir(Paths.PROJECT_ROOT):
            # Verify file is a json file
            if not project.endswith(".json"):
                continue
            # Load project
            cls._projects[project.replace(".json", "")] = Project(Paths.PROJECT_ROOT + Paths.SEPARATOR + project)

    # Get project from id
    @classmethod
    def get_project(cls, project_id: str):
        # Verify project exists
        if project_id not in cls._projects.keys():
            return None
        return cls._projects[project_id]

    # Get all projects
    @classmethod
    def get_projects(cls):
        return cls._projects.keys()