from secret_key import secret_key

# Configure Flask web_app object
class Config(object):
  SECRET_KEY = secret_key
  TEMPLATES_AUTO_RELOAD = True # Templates reload without needing to restart server
  SEND_FILE_MAX_AGE_DEFAULT = 0 # Set cache memory hours to 0: https://stackoverflow.com/a/54422901/6322172
