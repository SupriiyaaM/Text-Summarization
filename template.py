import os
from pathlib import Path
import logging #log all the information during runtime as well


'''
create logging stream :configures the logging module
format example:[2024-06-12 10:00:00]: This is an info message:
logging level determines the severity of the messages that the logger will handle
'''
logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "TextSummarizer"

#git: automatically takes code after commit and deploys it to cloud

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__/py",
    f"src/{project_name}/components/__init__/py",
    f"src/{project_name}/utils/__init__/py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__/py",
    f"src/{project_name}/config/_init__/py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__/py",
    f"src/{project_name}/entity/__init__/py",
    f"src/{project_name}/contants/__init__/py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile", #docker image of source code
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    #first create folders and then the files; both are returned below
    filedir, filename = os.path.split(filepath) 
    
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True) #will not create if already exists
        logging.info(f"Creating Directory: {filedir} for file: {filename}")
        
    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:      #writing mode
            pass
        logging.info(f"{filename} is being created")
        
    else:
         logging.info(f"{filename} is already created")