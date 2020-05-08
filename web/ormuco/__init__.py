# Imports
import os

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

from .model import Preference, db

# Create application
app = Flask(__name__)

# Gather application configuration
app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY', default='dev'),
)
app.config.from_pyfile('config.py', silent=True)

# Register SQLAlchemy extension
db.init_app(app)

# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Home route
# When form is submitted (POST method), we check submitted data,
# show errors if needed, save to database if everything is fine
@app.route('/', methods=('GET', 'POST'))
def preference():
    if request.method == 'POST':
        name = request.form['name']
        color = request.form['color']
        animal = request.form['animal']
        error = None

        if not name.strip():
            error = 'Name is required.'
        elif not color.strip():
            error = 'Color is required.'
        elif not animal or animal not in app.config['ANIMALS']:
            error = 'Animal is required and should match predefined values.'
        elif Preference.query.filter_by(name=name).first():
            error = 'Name is already taken.'

        if error is None:
            preference = Preference(
              name=name.strip(), color=color.strip(), animal=animal
            )
            db.session.add(preference)
            db.session.commit()
            flash("Successfully saved!", 'success')
            return redirect(url_for('preference'))

        flash(error, 'error')
    return render_template('preference.html', animals=app.config['ANIMALS'])
