from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
from src.Exception import CustomException
import sys
from src.logging.logger import get_logger

logging = get_logger(__name__)

try:
    data_ingestion  = DataIngestionPipeline()
    data_ingestion.main()
    logging.info("data ingestion pipeline finished")

    data_transformation =DataTransformationPipeline()
    data_transformation.main()
    logging.info("Tokenization Pipeline finished")


    #model_train = ModelTrainerPipeline()
    #model_train.train()
    #logging.info("Training pipeline finshed")

    model_evaluate = ModelEvaluationPipeline()
    model_evaluate.evaluate()
    logging.info("Evaluation pipeline finished")

except Exception as e :
    error = CustomException(e,sys)
    logging.error(error)
    raise error








