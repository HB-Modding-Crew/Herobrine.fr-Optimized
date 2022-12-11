#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK
# Must be first line
from __future__ import annotations
# Modules manager class
from src.steps_types.StepsTypesManager import StepsTypesManager
from src.projects.ProjectsManager import ProjectsManager
from src.workflows.WorkflowManager import WorkflowsManager
# Python libs
from argparse import ArgumentParser
from typing import Dict
import argcomplete
# Conventional imports
from src.actions import *

# Load modules
StepsTypesManager.load_steps()
WorkflowsManager.load_workflows()
ProjectsManager.load_projects()

class CommandLineTool:

    # Promary actions list
    _primary_actions: Dict[str, AActions] = {"execute": ExecuteAction}

    # List of arguments
    _arguments = {
        "action": {
            "positional": True,
            "required": True,
            "help": "Action to execute",
            "choices": _primary_actions.keys(),
        },
        "project": {
            "positional": False,
            "required": False,
            "help": "Project to execute the action on",
            "choices": ProjectsManager.get_projects(),
            "short": "-p"
        },
        "workflow": {
            "positional": False,
            "required": False,
            "help": "Workflow to execute the action on",
            "choices": WorkflowsManager.get_workflows(),
            "short": "-w"
        },
        "step": {
            "positional": False,
            "required": False,
            "help": "Step to execute the action on",
            "choices": StepsTypesManager.get_steps_types(),
            "short": "-s"
        },
    }


    # Init tool
    def __init__(self):
        # Init parser
        self._arg_parser = ArgumentParser(prog="creator", description="Help you create and maintain your modpack", epilog="Read the documentation for more information")
        # Add arguments
        self._add_arguments()

    # Add all arguments
    def _add_arguments(self):
        # For all arguments
        for argument_id in self._arguments.keys():
            # Get argument
            arg = self._arguments[argument_id]
            # Add argument
            if arg["positional"]:
                self._arg_parser.add_argument(argument_id, help=arg["help"], choices=arg["choices"])
            else:
                if "short" in arg.keys():
                    self._arg_parser.add_argument(arg["short"], "--" + argument_id, help=arg["help"], choices=arg["choices"], required=arg["required"])
                else:
                    self._arg_parser.add_argument("--" + argument_id, help=arg["help"], choices=arg["choices"], required=arg["required"])

        # Auto complete
        argcomplete.autocomplete(self._arg_parser)

    # Run tool
    def run(self):
        # Args
        args = vars(self._arg_parser.parse_args())
        # Action
        action_txt = args["action"]
        # Instanciate action
        action: AActions = self._primary_actions[action_txt](self._arg_parser)
        # Execute action
        action.execute(args)

tool = CommandLineTool()

# If this file is the main file
if __name__ == "__main__":
    # Run tool
    tool.run()