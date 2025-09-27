from src.entity import DataTransformationConfig
from transformers import AutoTokenizer
from datasets import load_dataset , load_from_disk 
from src.logging.logger import get_logger
import os 
import sys 

logging = get_logger(__name__)

class DataTransfomation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)


    def tokenization(self,example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'],max_length = 1000,truncation=True)

        with self.tokenizer.as_target_tokenizer():
            output_encodings = self.tokenizer(example_batch['summary'],max_length = 120 , truncation = True)


        return {
            'input_ids':input_encodings['input_ids'],
            'attention_mask':input_encodings['attention_mask'],
            'labels':output_encodings['input_ids']
        }
    

    def apply_tokenization(self):

        sam_data = load_from_disk(self.config.data_path)
        logging.info("data loaded from disk for tokenization")
        sam_data_tk = sam_data.map(self.tokenization,batched=True)
        logging.info("data tokenized")
        sam_data_tk.save_to_disk(self.config.transformed_path)
        logging.info("transformed data saved")
    