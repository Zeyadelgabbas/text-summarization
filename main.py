import torch
print("Torch version:", torch.__version__)
print("CUDA available?:", torch.cuda.is_available())
print("CUDA device count:", torch.cuda.device_count())



from src.logging.logger import get_logger

logging = get_logger(__name__)

logging.info('this is the main')