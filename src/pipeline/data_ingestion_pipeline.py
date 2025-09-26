
from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.logging.logger import get_logger
from src.Exception import CustomException
import sys

logging = get_logger(__name__) 
class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):

        try: 
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_and_extract()
            #data_ingestion.download_data()

            #data_ingestion.extract_zipfile()


        except Exception as e :
            error = CustomException(e,sys)
            logging.error(error)
            raise error