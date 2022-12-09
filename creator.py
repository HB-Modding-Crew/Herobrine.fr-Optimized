#!/usr/bin/env python3

from argparse import ArgumentParser
from src.const import Paths
import os
from src.workflows.Workflow import Workflow
from src.steps.StepsManager import StepsManager
from typing import List

class CommandLineTool:
    # Init tool
    def __init__(self):
        # Init parser
        self._arg_parser = ArgumentParser(prog="creator", description="Help you create and maintain your modpack", epilog="Read the documentation for more information")
        
        # Init steps manager
        StepsManager.load_steps()

        # Load workflow list
        self._load_workflow_list()

        # Workflow id list
        workflow_id_list = [workflow.id for workflow in self._workflow_list]

        # Add arguments
        # Add non optional positional argument workflow
        self._arg_parser.add_argument("workflow", help="Workflow to execute", choices=workflow_id_list)

    # Load workflow list
    def _load_workflow_list(self):
        # List of workflows
        self._workflow_list = []
        # Find all .json files in workflows folder
        for workklow_file in os.listdir(Paths.WORKFLOW_ROOT):
            # Verify file is a json file
            if not workklow_file.endswith(".json"):
                continue
            # Load workflow
            self._workflow_list.append(Workflow(Paths.WORKFLOW_ROOT + Paths.SEPARATOR + workklow_file))
        

    # Run tool
    def run(self):
        # Parse arguments
        args = self._arg_parser.parse_args()
        # Verify that workflow argument is not empty
        if args.workflow is None:
            print("Workflow argument is empty")
            return
        # Get workflow
        workflow = [workflow for workflow in self._workflow_list if workflow.id == args.workflow][0]
        # Execute workflow
        workflow.execute()

# If this file is the main file
if __name__ == "__main__":
    # Run tool
    CommandLineTool().run()