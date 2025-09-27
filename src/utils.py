import os 
import sys
import yaml
from box import ConfigBox
from src.Exception import CustomException
from src.logging.logger import get_logger
from ensure import ensure_annotations
from pathlib import Path
import torch


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



def get_safe_batch_size(default=2):
    if torch.cuda.is_available():
        free_mem, total_mem = torch.cuda.mem_get_info(0)
        free_gb = free_mem / (1024**3)

        print(f"GPU Free Memory: {free_gb:.2f} GB")

        if free_gb > 20:
            return 16
        elif free_gb > 12:
            return 8
        elif free_gb > 8:
            return 4
        elif free_gb > 4:
            return 2
        else:
            return 1
    else:
        print(" CUDA not available, falling back to CPU. Training will be slow.")
        return default