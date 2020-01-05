
from dotenv import load_dotenv
load_dotenv()
#import utils.index as messagequenue
import queues.index as sqs



sqs['sqs']()

# custom = config['custom']
# load_dotenv()

# mapping = {
#     'sqs': 'send_email_sqs',
#     'redis': 'send_email_redis'
# }

# messagequenue[mapping[custom['queue']]]()


