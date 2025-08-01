import os
import logging
from pathlib import Path

logging.basicConfig(level = logging.INFO, format = ('[%(asctime)s]: %(message)s:'))


project_name = "smartCity"

list_of_files = [
    f"{project_name}/agents/__init__.py",
    f"{project_name}/agents/classifier_agent.py",
    f"{project_name}/agents/traffic_agent.py",
    f"{project_name}/agents/health_agent.py",
    f"{project_name}/agents/utility_agent.py",
    f"{project_name}/agents/planner_agent.py",
    "langgraph_workflow/support_graph.py",
    "main.py",
    "langsmith_setup.py",
    "requirements.txt",
    "setup.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created Directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (not os.path.getsize(filepath) == 0):
        with open (filepath, "w") as f:
            pass
        logging.info(f"Created empty file {filepath}")
    else:
        logging.info(f"{filepath} already exists")
