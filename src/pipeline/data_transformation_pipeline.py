from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransfomation
from src.Exception import CustomException
import sys

class DataTransformationPipeline:

    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransfomation(config = data_transformation_config)
            data_transformation.apply_tokenization()
        except Exception as e:
            error = CustomException(e,sys)
            raise error