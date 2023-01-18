from src.Step.AStep import AStep
from src.const import Paths
import os
import json

class Step(AStep):

    def __update_project_curseforge_instance_path(self, new_path: str):
        # Open project file
        with open(self.project_file_path, "r") as project_file:
            # Read project file
            project_file_content = project_file.read()
            # Convert project file content to json
            project_file_json = json.loads(project_file_content)
        with open(self.project_file_path, "w") as project_file:
            # Update project curseforge instance path
            project_file_json["variables"]["curseforge_instance"] = new_path
            # Make json pretty
            project_file_json = json.dumps(project_file_json, indent=4)
            # Write project file
            project_file.write(project_file_json)
        # Log project file updated
        self.log("Project file updated with new curseforge instance path: " + new_path)

    def __update_project_minecraft_version(self, new_version: str):
        # Open project file
        with open(self.project_file_path, "r") as project_file:
            # Read project file
            project_file_content = project_file.read()
            # Convert project file content to json
            project_file_json = json.loads(project_file_content)
        with open(self.project_file_path, "w") as project_file:
            # Update project version
            project_file_json["variables"]["minecraft_version"] = new_version
            # Make json pretty
            project_file_json = json.dumps(project_file_json, indent=4)
            # Write project file
            project_file.write(project_file_json)
        # Log project file updated
        self.log("Project file updated with new minecraft version: " + new_version)

    def _execute(self) -> bool:
        # Log retrieve project id
        self.log("Retrieve project id...")
        # Get project id
        project_id = self.step_variables.project_id
        # Log project id
        self.log("Project id: " + project_id)
        # Project file name
        self.project_file_path = Paths.PROJECTS_ROOT + Paths.SEPARATOR + str(project_id) + ".json"
        # Log project file path
        self.log("Project file path: " + self.project_file_path)
        # Verify project file exists
        if not os.path.exists(self.project_file_path):
            # Log project file not found
            self.log(f"Project file ({self.project_file_path}) not found")
            # Return false
            return False
        # Curseforge instance path
        curseforge_instance_path_name = input("Instance directory name: ")
        curseforge_instance_path = self.step_variables["curseforge_instances_directory"] + Paths.SEPARATOR + curseforge_instance_path_name
        # Verify if curseforge instance path exists as directory
        if not os.path.isdir(curseforge_instance_path):
            # Log curseforge instance path not found
            self.log(f"Curseforge instance path ({curseforge_instance_path}) not found")
            # Return false
            return False
        # Log curseforge instance path found
        self.log(f"Curseforge instance path found: {curseforge_instance_path}")
        # Open curseforge instance file
        with open(curseforge_instance_path + Paths.SEPARATOR + "manifest.json", "r") as curseforge_instance_file:
            # Read curseforge instance file
            curseforge_instance_file_content = curseforge_instance_file.read()
            # Convert curseforge instance file content to json
            curseforge_instance_file_json = json.loads(curseforge_instance_file_content)
            # Get minecraft version
            minecraft_version = curseforge_instance_file_json["minecraft"]["version"]
            # Log minecraft version found
            self.log(f"Minecraft version found: {minecraft_version}")
        # Update project minecraft version
        self.__update_project_minecraft_version(minecraft_version)
        # Update project curseforge instance path
        self.__update_project_curseforge_instance_path(curseforge_instance_path_name)
        # Return true
        return True

    def _cancel(self):
        # Log impossible to cancel
        self.log("Impossible to cancel")
        # Ask to modify by hand project file or to rerun step
        self.log("You can modify by hand the project file or try rerun this step")


