from app import web_app
from flask import render_template

@web_app.route('/')
def index():
  return render_template('index.html')
