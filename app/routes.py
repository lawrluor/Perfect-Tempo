from app import web_app
from flask import render_template, flash, redirect, url_for
from app.forms import NumberForm

@web_app.route('/', methods=["GET", "POST"])
def index():
  form = NumberForm()
  if form.validate_on_submit():
    guess = form.bpm.data
    flash('You submitted: {}'.format(guess))
    return redirect('/') # redirect(url_for('index'))
  return render_template('index.html', form=form)
