import os
import sys
config = {
    'custom': {
        'queue': os.getenv("QUEUE"),
        'port': os.getenv("PORT"),
        'mariadb_master_url': os.getenv('MARIADB_MASTER_URL'),
        'redis_host': os.getenv('REDIS_HOST'),
        'redis_password': os.getenv('REDIS_PASSWORD'),
        'redis_db': os.getenv('REDIS_DB'),
        'redis_prefix': os.getenv('REDIS_PREFIX'),
        'aws_access_key_id': os.getenv('AWS_ACCESS_KEY_ID'),
        'aws_secret_access_id': os.getenv('AWS_SECRET_ACCESS_KEY'),
        'aws_region': os.getenv('AWS_REGION'),
        'queue_name': os.getenv('QUEUE_NAME'),
        'queue': os.getenv('QUEUE'),
        'email': os.getenv('EMAIL'),
        'stmp_username': os.getenv('SMTP_USERNAME'),
        'stmp_password': os.getenv('SMTP_PASSWORD'),
        'stmp_host': os.getenv('SMTP_HOST'),
        'email_to': os.getenv('EMAIL_TO')
    },
    'default': {
        'queue': os.getenv("QUEUE"),
        'port': os.getenv("PORT"),
        'mariadb_master_url': os.getenv('MARIADB_MASTER_URL'),
        'redis_host': os.getenv('REDIS_HOST'),
        'redis_password': os.getenv('REDIS_PASSWORD'),
        'redis_db': os.getenv('REDIS_DB'),
        'redis_prefix': os.getenv('REDIS_PREFIX'),
        'aws_access_key_id': os.getenv('AWS_ACCESS_KEY_ID'),
        'aws_secret_access_id': os.getenv('AWS_SECRET_ACCESS_KEY'),
        'aws_region': os.getenv('AWS_REGION'),
        'queue_name': os.getenv('QUEUE_NAME'),
        'queue': os.getenv('QUEUE'),
        'email': os.getenv('EMAIL'),
        'stmp_username': os.getenv('SMTP_USERNAME'),
        'stmp_password': os.getenv('SMTP_PASSWORD'),
        'stmp_host': os.getenv('SMTP_HOST'),
        'email_to': os.getenv('EMAIL_TO')
    }
}

sys.modules[__name__] = config
