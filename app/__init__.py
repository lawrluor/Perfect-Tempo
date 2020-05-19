from flask import Flask # import Flask Class from flask module
from config import Config # import Config Class from config.py

web_app = Flask(__name__) # Initialize Flask web application object
web_app.config.from_object(Config) # Use configurations from config.py

# NOTE: This needs to be imported at the end to prevent circular dependency
from app import routes # folder in which the routes (urls) are created
