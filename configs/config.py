from dataclasses import dataclass
import os

@dataclass
class default:

    queue:str= os.getenv("QUEUE")
    port:str= os.getenv("PORT")
    mariadb_master_url:str= os.getenv('MARIADB_MASTER_URL')
    redis_host:str= os.getenv('REDIS_HOST')
    redis_password:str= os.getenv('REDIS_PASSWORD')
    redis_db:str= os.getenv('REDIS_DB')
    redis_prefix:str= os.getenv('REDIS_PREFIX')
    aws_access_key_id:str= os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_id:str= os.getenv('AWS_SECRET_ACCESS_KEY')
    aws_region:str= os.getenv('AWS_REGION')
    queue_name:str= os.getenv('QUEUE_NAME')
    queue:str= os.getenv('QUEUE')
    email:str= os.getenv('EMAIL')
    stmp_username:str= os.getenv('SMTP_USERNAME')
    stmp_password:str= os.getenv('SMTP_PASSWORD')
    stmp_host:str= os.getenv('SMTP_HOST')
    email_to:str= os.getenv('EMAIL_TO')
