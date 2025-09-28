from transformers import pipeline , AutoTokenizer , AutoModelForSeq2SeqLM

from src.config.configuration import ConfigurationManager


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,text):

        config = ConfigurationManager().get_evaluation_config()
        model = AutoModelForSeq2SeqLM.from_pretrained(config.model_path)
        tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_path)
        gen_kwargs = {"length_penalty":0.8,"num_beams":8,"max_length":128}
        pipe = pipeline('summarization',model=model , tokenizer=tokenizer)
        
        print("Dialogue : ")
        print(text)

        output = pipe(text,**gen_kwargs)[0]['summary_text']
        print("summary: ")
        print(output)

        return output