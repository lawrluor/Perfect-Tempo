from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


# Allows User to guess BPM (integer within specific range)
# Handling two submitFields in a form: https://stackoverflow.com/questions/35774060/determine-which-wtforms-button-was-pressed-in-a-flask-view/35776874
class GuessForm(FlaskForm):
  bpm = IntegerField('BPM:', validators=[
    NumberRange(0, 255, u'Please enter a number between 0-255'),
  ])
  submit = SubmitField('Guess')
  play = SubmitField('Play Sound')
