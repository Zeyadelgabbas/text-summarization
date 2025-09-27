from src.logging.logger import get_logger
from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.Exception import CustomException
import sys
from src.pipeline.data_transformation_pipeline import DataTransformationPipeline


logging = get_logger(__name__)

try:
    data_ingestion  = DataIngestionPipeline()
    data_ingestion.main()
    logging.info("data ingestion pipeline finished")

    data_transformation =DataTransformationPipeline()
    data_transformation.main()
    logging.info("Tokenization Pipeline finished")

except Exception as e :
    error = CustomException(e,sys)
    logging.error(error)
    raise error







