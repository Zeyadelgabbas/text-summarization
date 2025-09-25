import os 
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO,format = '[%(asctime)s]  : %(message)s:')


list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/pipeline/__init__.py",
    "src/utils.py",
    "src/logging/__init__.py",
    "src/config/configuration.py",
    "src/config/__init__.py",
    "src/constants/__init__.py",
    "src/entity/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "requirements.txt",
    "setup.py",
    "Notebooks/trials.ipynb",
    "src/Exception.py",

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir ,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating dir {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize ==0):
        with open(filepath,"w") as f :
            pass

    else:
        logging.info(f"file {filename} already exists")

