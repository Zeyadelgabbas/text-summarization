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