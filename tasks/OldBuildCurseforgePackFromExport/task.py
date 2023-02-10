from ModpackCreator.ATask import ATask
from ModpackCreator.ATask import AVarDef
from ModpackCreator.InputVarTypes.PathVar import RelativeToPathVar
import os
import re
from ModpackCreator.BuiltInTasks.BuildCurseforgePackFromExport.task import ModpackNameVar
from ModpackCreator.BuiltInTasks.BuildCurseforgePackFromExport.task import VersionVar
from ModpackCreator.BuiltInTasks.BuildCurseforgePackFromExport.task import CurseforgeInstanceExportPathVar
from ModpackCreator.BuiltInTasks.BuildCurseforgePackFromExport.task import Task as OTask

from . import FilesFunctions
import json


class Task(OTask):

    # Prepared export paths
    curseforge_prepared_export_path = "temp/curseforge_prepared_export.zip"
    mmc_prepared_export_path = "temp/mmc_prepared_export.zip"

    # Setup configs list
    setup_configs = [
        ModpackNameVar("modpack_name", "Name of the modpack", passive=True),
    ]

    # Run variables
    run_args = [
        CurseforgeInstanceExportPathVar("curseforge_instance_export_path", "Path to the curseforge instance .zip export"),
        VersionVar("version", "New version of the pack")
    ]

    def prepare_curseforge_profile(self):
        # Execute super
        super().prepare_curseforge_profile()

        # Log removal of config and keep only config/yosbr
        print(f"Removing config and keeping only overrides/config/yosbr")

        # Copy overrides/config/yosbr from zip to temp
        FilesFunctions.copy_dir_from_zip("overrides/config/yosbr", "temp/yosbr", self.curseforge_prepared_export_path)

        # Remove overrides config from zip
        if FilesFunctions.zip_contains_dir(self.curseforge_prepared_export_path, "overrides/config"):
            FilesFunctions.remove_dir_from_zip("overrides/config", self.curseforge_prepared_export_path)

        # Copy overrides/config/yosbr from temp to zip
        FilesFunctions.copy_dir_to_zip("temp/yosbr", "overrides/config/yosbr", self.curseforge_prepared_export_path)
