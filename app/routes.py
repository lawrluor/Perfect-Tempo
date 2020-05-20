from app import web_app
from flask import flash, session, redirect, render_template, url_for
from app.forms import GuessForm, PlayForm

import random
import os

# States
  # started=False means User has just loaded page, or has just guessed the last BPM correctly. Don't display the BPM form, and don't play the sample
  # started=False -> started=True: User indicates that they are ready by clicking the Play button
  # started=True means that the User has begun guessing, and can now guess. Display the BPM guess form and replay the sample after each incorrect guess
  # started=True -> started=False: The User guesses the last BPM correctly, and reads the message. They can continue onto the next sample by clicking Play button.

@web_app.route('/', methods=["GET", "POST"])
def index():
  guess_form = GuessForm()
  play_form = PlayForm()

  if 'target' not in session:
    session['target'] = random.randint(120, 131)

  if 'guesses' not in session:
    session['guesses'] = 0

  if 'started' not in session:
    session['started'] = False

  print('Started: {}, Target: {}'.format(session['started'], session['target']))

  # TODO: Play is always being submitted
  # Ideally, only check guess form if Play was NOT submitted (play button was not clicked)
  play = guess_form.play.data
  if guess_form.play.data:
    print("play pressed:", play)
    # print('play form clicked', play_form.submit.data)
    session['started'] = True
  else:
    print('guess pressed:', guess_form.submit.data)
    if guess_form.validate_on_submit():
      guess = guess_form.bpm.data

      if guess==session['target']:
        # If guessed right: Then reset target, guesses, and redirect
        flash('Correct! You guessed: {}. The bpm was: {}'.format(guess, session['target']))
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
    play_form=play_form,
    guesses=session['guesses'],
    target=str(session['target']),
    started=session['started']
  )


@web_app.route('/about')
def about():
  return render_template('about.html', title='About')


# Not used at the moment - just for playing local MIDI
@web_app.route('/play')
def play():
  print(os.getcwd())
  output = mido.open_output(name='foo', virtual=True)
  file_name = os.path.join(os.path.dirname(__file__), 'test.mid') # See https://stackoverflow.com/q/43652767/6322172
  for message in MidiFile(file_name).play():
    output.send(message)

  return render_template('about.html', title='Play')
