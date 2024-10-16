import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO ,format='[%(asctime)s]:%(message)s')

project="wine_project"

list_of_files=[
   f"src/{project}/__init.py__",
   f"src/{project}/components/__init.py__",
   f"src/{project}/utils/common.py",
   f"src/{project}/config/__init.py__",
   f"src/{project}/config/configuration.py",
   f"src/{project}/pipeline/__init.py__",
   f"src/{project}/entity/__init.py__",
   f"src/{project}/entity/config_entity.py",
   f"src/{project}/constant/__init.py__",
   "config/config.yaml",
   "praram.yaml",
   "schema.yaml",
   "main.py",
   "app.py",
   "requirement.txt",
   "setup.py",
   "research/trial.ipynb",
   "template/index.html"


]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory;{filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file{filepath}")
    else:
        logging.info(f"file {filepath} already exist")