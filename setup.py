#!/usr/bin/env python3

import shutil
from src.const import Paths

# Copy default steps to steps folder
print("Copying default steps to steps folder")
shutil.copytree(Paths.DEFAULT_STEPS_ROOT, Paths.STEPS_TYPE_ROOT, dirs_exist_ok=True)

# Copy default workflows to workflows folder
print("Copying default workflows to workflows folder")
shutil.copytree(Paths.DEFAULT_WORKFLOW_ROOT, Paths.WORKFLOW_ROOT, dirs_exist_ok=True)