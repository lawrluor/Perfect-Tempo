from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# Allows User to guess BPM (integer within specific range)
class GuessForm(FlaskForm):
  bpm = IntegerField('BPM:', validators=[
    NumberRange(0, 255, u'Please enter a number between 0-255'),
  ])
  submit = SubmitField('Guess')
  play = SubmitField('Play')

# Play Button
class PlayForm(FlaskForm):
  submit = SubmitField('Play')
