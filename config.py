import os
from secret_key import secret_key

# Configure Flask web_app object
class Config(object):
  SECRET_KEY = secret_key
  TEMPLATES_AUTO_RELOAD = True # Templates reload without needing to restart server
  SEND_FILE_MAX_AGE_DEFAULT = 0 # Set cache memory hours to 0: https://stackoverflow.com/a/54422901/6322172

  MAIL_SERVER = os.environ.get('MAIL_SERVER')
  MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
  MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  ADMINS = ['luolawrence1@gmail.com']
