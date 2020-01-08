from dotenv import load_dotenv
load_dotenv()
from configs.config import default
import queues.index as sqs

sqs[default.queue]() 



