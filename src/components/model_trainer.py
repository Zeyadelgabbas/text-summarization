import os
import torch
from transformers import AutoTokenizer,AutoModelForSeq2SeqLM , Trainer , TrainingArguments , DataCollatorForSeq2Seq , EarlyStoppingCallback
from datasets import load_from_disk
from src.logging.logger import get_logger
from src.Exception import CustomException
import sys
from dataclasses import asdict
from src.utils import get_safe_batch_size
from src.entity import ModelTrainerConfig
logging = get_logger(__name__)


class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):

        self.config = config


    def train(self):
        device = 'cuda' if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer , model = model_pegasus)
        dataset = load_from_disk(self.config.data_path)

        """
        dic_debug = asdict(self.config)
        for key, value in dic_debug.items():
            print(key, value, type(value))
        
        """
    
        training_args = TrainingArguments(
    per_device_train_batch_size = get_safe_batch_size(),
    per_device_eval_batch_size = get_safe_batch_size(),
    learning_rate = self.config.learning_rate,
    warmup_steps = self.config.warmup_steps,
    weight_decay = self.config.weight_decay,
    eval_strategy = self.config.eval_strategy,
    save_strategy = self.config.save_strategy,
    save_total_limit = self.config.save_total_limit,
    logging_steps = self.config.logging_steps,
    eval_steps = self.config.eval_steps,
    load_best_model_at_end = self.config.load_best_model_at_end,
    metric_for_best_model = self.config.metric_for_best_model,
    gradient_accumulation_steps = self.config.gradient_accumulation_steps,
    num_train_epochs = self.config.num_train_epochs,
    output_dir = self.config.root_dir,
    fp16=True
)

        trainer = Trainer(model = model_pegasus , args = training_args ,
                           tokenizer = tokenizer , data_collator=data_collator ,
                           train_dataset=dataset["train"],
                           eval_dataset=dataset["validation"] ,
                           callbacks=[EarlyStoppingCallback(early_stopping_patience=6)]
                           )
        trainer.train()
        logging.info("model training finished")
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))
        logging.info("model and tokenizer saved")
        
