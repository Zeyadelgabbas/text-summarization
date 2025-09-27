
from src.config.configuration  import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation



class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def evaluate(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()

