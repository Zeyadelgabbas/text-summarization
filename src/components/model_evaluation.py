
from transformers import AutoTokenizer , AutoModelForSeq2SeqLM
import evaluate
from datasets import load_from_disk
from src.entity import ModelEvaluationConfig
from tqdm import tqdm
import torch
import pandas as pd

from src.logging.logger import get_logger
logging = get_logger(__name__)

class ModelEvaluation:
    
    def __init__(self,config:ModelEvaluationConfig):
        self.config = config


    def generate_batch_chuncks(self,full_data,batch_size):

        for i in range(0,len(full_data),batch_size):
            yield full_data[i:i+batch_size]


    def calculate_metrics_test(self,dataset,metric,tokenizer,model, input_name, target_name,device ,batch_size = 16 ):

        
        input_batches = list(self.generate_batch_chuncks(dataset[input_name],batch_size))
        target_batches = list(self.generate_batch_chuncks(dataset[target_name],batch_size))

        for input_batch , target_batch in tqdm(zip(input_batches,target_batches),total=len(input_batches)):
            inputs = tokenizer(input_batch, max_length=1024, truncation=True, 
                   padding="max_length", return_tensors="pt")
            
            summary = model.generate(input_ids=inputs["input_ids"].to(device),
                           attention_mask=inputs["attention_mask"].to(device), 
                           length_penalty=0.8, num_beams=8, max_length=128)
            
            decoded_summary = [tokenizer.decode(s, skip_special_tokens=True, 
                                      clean_up_tokenization_spaces=True) 
                     for s in summary]      
            #decoded_summary = [d.replace("", " ") for d in decoded_summary]

            metric.add_batch(predictions=decoded_summary, references=target_batch)
        
        final_score = metric.compute()
        return final_score
    
    def evaluate(self):

        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)
        rouge = evaluate.load("rouge")
        
        dataset_pt = load_from_disk(self.config.data_path)
        input_name = 'dialogue'
        target_name = 'summary'

        scores = self.calculate_metrics_test(
            dataset=dataset_pt['test'][0:300] , metric = rouge , tokenizer=tokenizer , 
            model=model,input_name = input_name,target_name = target_name ,device  = device 
        )
        logging.info("Metrics scores calculated")

        rouge_metrics = ['rouge1','rouge2','rougeL','rougeLsum']

        rouge_dict = dict((metric, scores[metric]) for metric in rouge_metrics )

        df = pd.DataFrame(rouge_dict, index = ['pegasus'] )
        df.to_csv(self.config.metric_filename, index=False)

        logging.info(f"metric score saved to {self.config.metric_filename}")

        
        