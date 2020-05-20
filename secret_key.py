import os

secret_key = os.environ.get('SECRET_KEY') or "This secret key is used by config.py. Best practice is to set it using the environment variable SECRET_KEY"
