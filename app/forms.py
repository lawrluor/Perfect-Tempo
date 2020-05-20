from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class NumberForm(FlaskForm):
  bpm = IntegerField('BPM', validators=[DataRequired()])
  submit = SubmitField('Guess')

class PlayForm(FlaskForm):
  submit = SubmitField('Play')
