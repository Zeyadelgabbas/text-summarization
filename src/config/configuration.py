from src.constants import *
from src.utils import read_yaml , create_directory
from src.entity import DataIngestionConfig , DataTransformationConfig , ModelTrainerConfig , ModelEvaluationConfig

class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILE_PATH , params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directory([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion

        create_directory([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir ,
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_transformation_config(self):
        config = self.config.data_transformation

        create_directory([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            data_path = config.data_path,
            root_dir = config.root_dir, 
            tokenizer_name=config.tokenizer_name,
            transformed_path=config.transformed_path
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) ->ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.TrainingParameters

        create_directory([config.root_dir])
        config = ModelTrainerConfig(
                    root_dir = config.root_dir,
                    data_path = config.data_path,
                    model_ckpt = config.model_ckpt,
                    num_train_epochs = params.num_train_epochs,
                    per_device_train_batch_size = params.per_device_train_batch_size,
                    per_device_eval_batch_size = params.per_device_eval_batch_size,
                    learning_rate = params.learning_rate,
                    warmup_steps = params.warmup_steps,
                    weight_decay = params.weight_decay,
                    eval_strategy = params.eval_strategy,
                    save_strategy = params.save_strategy,
                    save_total_limit = params.save_total_limit,
                    logging_steps = params.logging_steps,
                    eval_steps = params.eval_steps,
                    load_best_model_at_end = params.load_best_model_at_end,
                    metric_for_best_model = params.metric_for_best_model,
                    gradient_accumulation_steps = params.gradient_accumulation_steps,
                )
        return config
    

    def get_evaluation_config(self) ->ModelEvaluationConfig:
        config = self.config.model_evaluation
        create_directory([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            model_path=config.model_path,
            data_path=config.data_path,
            root_dir=config.root_dir,
            tokenizer_path=config.tokenizer_path,
            metric_filename=config.metric_filename
        )
        return model_evaluation_config