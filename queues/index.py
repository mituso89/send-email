from queues.sqs import sqs
import sys

sys.modules[__name__] = {'sqs': sqs}
