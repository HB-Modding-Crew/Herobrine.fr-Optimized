from src.creator import Creator
import sys
from src.Step.StepTypesManager import StepTypesManager

# First argument is the project id
project_id = sys.argv[1]

# Second argument is the workflow id
workflow_id = sys.argv[2]

# Step types
StepTypesManager.load_steps_types()

# Init creator
creator = Creator()

# Execute workflow
creator.execute(project_id=project_id, workflow_id=workflow_id)

