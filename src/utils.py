import os 
import sys
import yaml
from box import ConfigBox
from src.Exception import CustomException
from src.logging.logger import get_logger
from ensure import ensure_annotations
from pathlib import Path

logging = get_logger(__name__)


@ensure_annotations
def read_yaml(yaml_path : Path):

    try:

        with open(yaml_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f'yaml file {yaml_path} loaded ')
            return ConfigBox(content)
    except Exception as e:
        error = CustomException(e,sys)
        logging.error(error)
        raise error
    
@ensure_annotations
def create_directory(dir_path : list):

    for path in dir_path:
        os.makedirs(path,exist_ok=True)

        logging.info(f"created directory {path}")