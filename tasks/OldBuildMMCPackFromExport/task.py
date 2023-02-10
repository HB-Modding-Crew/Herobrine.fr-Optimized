from ModpackCreator.BuiltInTasks.CurseForgeToMultiMC.task import MultiMCInstancePathVar
from ModpackCreator.BuiltInTasks.BuildCurseforgePackFromExport.task import ModpackNameVar
from ModpackCreator.BuiltInTasks.BuildMMCPackFromExport.task import VersionVar, MultiMCInstanceExportPathVar, Task as OTask

from . import FilesFunctions
import json
import re

class Task(OTask):

    # Prepared export paths
    curseforge_prepared_export_path = "temp/curseforge_prepared_export.zip"
    mmc_prepared_export_path = "temp/mmc_prepared_export.zip"

    # Setup configs list
    setup_configs = [
        MultiMCInstancePathVar("mmc_instance", "Path to the MMC instance folder", passive=True),
        ModpackNameVar("modpack_name", "Name of the modpack", passive=True)
    ]

    # Run variables
    run_args = [
        MultiMCInstanceExportPathVar("mmc_instance_export_path"),
        VersionVar("version", "New version of the pack")
    ]


    # Override prepare_mmc_profile
    def prepare_mmc_profile(self):
        print("Preparing MultiMC profile")
        # Version name regex
        name_value_regex = re.compile(r"\d+\.\d+\.\d+-?\w*\.?\d*")
        # Get instance name
        instance_name = self.config["mmc_instance"].split("/")[-1].split("\\")[-1]
        # Main menu crédits path
        main_menu_credits_path = f"config/yosbr/config/isxander-main-menu-credits.json"

        # Execute super
        super().prepare_mmc_profile()

        # Find minecraft folder name
        if FilesFunctions.zip_contains_dir(self.mmc_prepared_export_path, instance_name + "/.minecraft"):
            minecraft_folder_name = ".minecraft"
        elif FilesFunctions.zip_contains_dir(self.mmc_prepared_export_path, instance_name + "/minecraft"):
            minecraft_folder_name = "minecraft"
        else:
            raise Exception("Could not find minecraft folder in zip")

        # Log removal of config and keep only config/yosbr
        print(f"Removing config and keeping only {minecraft_folder_name}/config/yosbr")

        # Copy config/yosbr from zip to temp
        print("Copying config/yosbr from zip to temp")
        FilesFunctions.copy_dir_from_zip(instance_name + f"/{minecraft_folder_name}/config/yosbr", "temp/yosbr", self.mmc_prepared_export_path)

        # Remove overrides config from zip
        print("Removing config from zip")
        if FilesFunctions.zip_contains_dir(self.mmc_prepared_export_path, instance_name + f"/{minecraft_folder_name}/config"):
            FilesFunctions.remove_dir_from_zip(instance_name + f"/{minecraft_folder_name}/config", self.mmc_prepared_export_path)

        # Copy config/yosbr from temp to zip
        print("Copying config/yosbr from temp to zip")
        FilesFunctions.copy_dir_to_zip("temp/yosbr", instance_name + f"/{minecraft_folder_name}/config/yosbr", self.mmc_prepared_export_path)

        # Change version name
        # Copy isxander-main-menu-credits.json from zip to temp
        print("Copying isxander-main-menu-credits.json from zip to temp")
        FilesFunctions.copy_from_zip(instance_name + f"/{minecraft_folder_name}/{main_menu_credits_path}", "temp/isxander-main-menu-credits.json", self.mmc_prepared_export_path)

        # Read isxander-main-menu-credits.json
        print("Reading isxander-main-menu-credits.json")
        with open("temp/isxander-main-menu-credits.json", "r") as f:
            main_menu_credits = json.load(f)

        # Change version name
        print("Changing version name")
        main_menu_credits["main_menu"]["bottom_right"][0]["text"] = name_value_regex.sub(self.args["version"], main_menu_credits["main_menu"]["bottom_right"][0]["text"])

        # Write isxander-main-menu-credits.json
        print("Writing isxander-main-menu-credits.json")
        with open("temp/isxander-main-menu-credits.json", "w") as f:
            json.dump(main_menu_credits, f, indent=4)

        # Copy isxander-main-menu-credits.json from temp to zip
        print("Copying isxander-main-menu-credits.json from temp to zip")
        FilesFunctions.copy_to_zip("temp/isxander-main-menu-credits.json", instance_name + f"/{minecraft_folder_name}/{main_menu_credits_path}", self.mmc_prepared_export_path)
        
        
