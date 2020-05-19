from flask import Flask # import flask library from module

web_app = Flask(__name__) # Initialize Flask web application object

# NOTE: This needs to be imported at the end to prevent circular dependency
from app import routes # folder in which the routes (urls) are created
