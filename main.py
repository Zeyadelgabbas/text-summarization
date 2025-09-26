from src.logging.logger import get_logger
from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.Exception import CustomException
import sys


logging = get_logger(__name__)

try:
    data_ingestion  = DataIngestionPipeline()
    data_ingestion.main()
    logging.info("data ingestion completed")

except Exception as e :
    error = CustomException(e,sys)
    logging.error(error)
    raise error







