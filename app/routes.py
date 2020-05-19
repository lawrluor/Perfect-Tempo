from app import web_app
from flask import flash, session, redirect, render_template, url_for
from app.forms import NumberForm

import random
import mido
from mido import MidiFile
import os ;

@web_app.route('/', methods=["GET", "POST"])
def index():
  # session.clear()
  form = NumberForm()
  if 'target' not in session:
      session['target'] = random.randint(30, 256)

  # flash(session['target'])

  if form.validate_on_submit():
    guess = form.bpm.data
    flash('You submitted: {}. The bpm was: {}'.format(guess, session['target']))
    return redirect('/') # redirect(url_for('index'))
  return render_template('index.html', form=form, target=session['target'])

@web_app.route('/about')
def about():
  return render_template('about.html', title='About')

@web_app.route('/play')
def play():
  print(os.getcwd())
  output = mido.open_output(name='foo', virtual=True)
  file_name = os.path.join(os.path.dirname(__file__), 'test.mid') # See https://stackoverflow.com/q/43652767/6322172
  for message in MidiFile(file_name).play():
    output.send(message)

  return render_template('about.html', title='Play')
