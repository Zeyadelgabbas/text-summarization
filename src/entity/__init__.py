from dataclasses import dataclass
from pathlib import Path 

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_url : str
    local_data_file : Path
    unzip_dir : Path
    

@dataclass
class DataTransformationConfig:
     root_dir: Path
     data_path: Path
     tokenizer_name: str
     transformed_path : Path

@dataclass
class ModelTrainerConfig:
    #config 
    root_dir: Path
    data_path: Path
    model_ckpt: str
    #params
    num_train_epochs: int
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    learning_rate: float
    warmup_steps: int
    weight_decay: float
    eval_strategy: str
    save_strategy: str
    save_total_limit: int
    logging_steps: int
    eval_steps: int
    load_best_model_at_end: bool
    metric_for_best_model: str
    gradient_accumulation_steps: int


@dataclass
class ModelEvaluationConfig:

    model_path: Path
    data_path: Path
    root_dir: Path
    tokenizer_path: Path
    metric_filename: Path