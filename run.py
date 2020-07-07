#!env/bin/python
from app import web_app

# See Encapsulating the run: https://stackoverflow.com/a/29356488/6322172
# On Heroku, port 0.0.0.0 will be used by default
if __name__ == '__main__':
  web_app.run(debug=True) # port=
