
from utils.sqs import send_email_sqs
from utils.redis import send_email_redis
import sys

class poli():

    def send():
        return ''

# sys.modules[__name__] = {'send_email_sqs':send_email_sqs , 'send_email_redis':send_email_redis}
sys.modules[__name__] = send_email_sqs