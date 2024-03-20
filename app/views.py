"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField, FileField
from wtforms.validators import InputRequired
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from app.forms import PropertyForm
from app.models import Property



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route("/properties/create")
def create_properties():
    form = PropertyForm()
    if form.validate_on_submit():
        # Save uploaded file
        photo_filename = ''
        if form.photo.data:
            photo = form.photo.data
            photo_filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))
        
        # Create new property object and add it to the database
        new_property = Property(
            title=form.title.data,
            bedrooms=form.bedrooms.data,
            bathrooms=form.bathrooms.data,
            location=form.location.data,
            price=form.price.data,
            type=form.type.data,
            description=form.description.data,
            photo=photo_filename
        )
        db.session.add(new_property)
        db.session.commit()
        return redirect(url_for('properties'))

    return render_template('create_property.html', form=form)




@app.route("/properties")
def properties():
    properties = Property.query.all()
    return render_template('properties.html', properties=properties)

@app.route("/properties/<propertyid>")
###
# The functions below should be applicable to all Flask apps.
###
def view_properties(propertyid):
    property = Property.query.get_or_404(propertyid)
    return render_template('viewproperty.html', property=property)

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
