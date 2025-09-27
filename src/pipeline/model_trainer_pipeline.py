
from src.config.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer
from src.Exception import CustomException
import sys
from src.logging.logger import get_logger
logging = get_logger(__name__)


class ModelTrainerPipeline:
    def __init__(self):
        pass
    def train(self):

        try : 
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()

        except Exception as e :
            error = CustomException(e,sys)
            logging.error(error)
            raise error