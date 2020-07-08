from app import web_app
from flask import flash, session, redirect, render_template, url_for
from app.forms import GuessForm

import random
import os

# MIDI setup (local only)
import mido
from mido import MidiFile

# States
  # started=False means User has just loaded page, or has just guessed the last BPM correctly. Don't display the BPM form, and don't play the sample
  # started=False -> started=True: User indicates that they are ready by clicking the Play button
  # started=True means that the User has begun guessing, and can now guess. Display the BPM guess form and replay the sample after each incorrect guess
  # started=True -> started=False: The User guesses the last BPM correctly, and reads the message. They can continue onto the next sample by clicking Play button.

@web_app.route('/', methods=["GET", "POST"])
def index():
  guess_form = GuessForm()

  if 'target' not in session:
    session['target'] = random.randint(120, 131)

  if 'guesses' not in session:
    session['guesses'] = 0

  if 'started' not in session:
    session['started'] = False

  print('Started: {}, Target: {}'.format(session['started'], session['target']))

  if guess_form.play.data:
    print("play pressed") # Play button of guess_form was pressed
    session['started'] = True # Start game when play is pressed. Overwrites with True
  else:
    # Only check guess content if play button was NOT clicked
    # This is because if User wants to replay sound, it should only replay sound, not attempt to check their guess answer
    print("guess pressed") # Guess button of guess_form was pressed
    if guess_form.validate_on_submit():
      guess = guess_form.bpm.data

      if guess==session['target']:
        # If guessed right: Then reset target, guesses, and redirect
        flash('Correct! You guessed: {}. The BPM was: {}.'.format(guess, session['target']))
        session['target'] = random.randint(120, 130) # inclusive
        session['guesses'] = 0
        session['started'] = False
        return redirect(url_for('index'))
      else:
        # If guessed wrong: Increment guesses, but don't redirect
        flash('Incorrect. You guessed: {}.'.format(guess))
        session['guesses'] += 1
    else:
      print('guess_form not submitted')

  return render_template('index.html',
    guess_form=guess_form,
    guesses=session['guesses'],
    target=str(session['target']),
    started=session['started']
  )


@web_app.route('/about')
def about():
  return render_template('about.html', title='About')


# Just for playing local MIDI. Buggy.
@web_app.route('/playMidi')
def playMidi():
  output = mido.open_output(name='foo', virtual=True)
  file_name = os.path.join(os.path.dirname(__file__), 'static/midi/test.mid') # See https://stackoverflow.com/q/43652767/6322172
  print("Current Location:", os.getcwd())
  print("MidiFile:", file_name)

  for message in MidiFile(file_name).play():
    output.send(message)

  return render_template('about.html', title='Play')

# Error handling
@web_app.errorhandler(404) # for files not found
def error_404(error):
  return render_template('404.html'), 404

@web_app.errorhandler(500) # for internal errors
def error_500(error):
  # rollback action/DB
  return render_template('500.html'), 500
