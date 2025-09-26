import os
import urllib.request as request
import zipfile 
from src.logging.logger import get_logger
from src.entity import DataIngestionConfig

import requests , zipfile , io


logging = get_logger(__name__)

class DataIngestion:
    def __init__(self,config : DataIngestionConfig):
        self.config = config 

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(url = self.config.source_url, filename=self.config.local_data_file)

            logging.info(f"{filename} has been downloaded ! : \n {headers}")
        else:
            logging.info("file already exists")
    def extract_zipfile(self):
        unzip_path = self.config.unzip_dir

        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_file:
            zip_file.extractall(unzip_path)
    def download_and_extract(self):
        unzip_path = self.config.unzip_dir
        url = self.config.source_url
        os.makedirs(unzip_path, exist_ok=True)

        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with zipfile.ZipFile(io.BytesIO(r.content)) as zip_ref:
                zip_ref.extractall(unzip_path)

            