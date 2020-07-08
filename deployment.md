# Using:
* heroku
* pip for package management

# Steps for Initial Release:
1. Connected to Github
2. Create Procfile (see below)
3. Create Heroku Dyno
  * App Name (in Settings): https://perfect-tempo.herokuapp.com/

# BEFORE DEPLOYING FUTURE RELEASES:
**Set DEBUG_MODE in .flaskenv off.**
"It is extremely important that you never run a Flask application in debug mode on a production server. The debugger allows the user to remotely execute code in the server, so it can be an unexpected gift to a malicious user who wants to infiltrate your application or your server." - Miguel Grinberg

# Future Releases:
In Heroku, select `Deploy -> Manual Deploy` (currently deploying build code from master branch of Github)

# See Debug Logs:
$ heroku logs -a perfect-tempo


# Reference
Create Procfile: https://devcenter.heroku.com/articles/procfile

See https://stackoverflow.com/a/59702132/6322172 for formatting
```
web: gunicorn --bind 0.0.0.0:$PORT app:web_app
```

Last two parameters: the script that runs your app (__init__.py, NOT run.py), and the name of the app (in __init__.py)

See https://stackoverflow.com/a/29356488/6322172 for more details - basically using run.py attempts to run on another port when init is already running
