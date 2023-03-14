"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, send_from_directory, url_for, flash, session, abort
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from app.forms import AddForm
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

@app.route('/properties')
def properties():
    properties = db.session.execute(db.select(Property)).scalars()
    return render_template('properties.html', properties=properties)

@app.route('/properties/create', methods=['POST', 'GET'])
def new_property():
    addform = AddForm()
    file_folder = app.config['UPLOAD_FOLDER']

    if request.method == 'POST':
    #validate on submit
        if addform.validate_on_submit():
            photo = addform.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(file_folder, filename))

            property = Property(
                proptitle=addform.proptitle.data,
                description=addform.description.data,
                number_of_rooms=addform.number_of_rooms.data,
                price=addform.price.data,
                location=addform.location.data,
                photo=filename,
                number_of_bathrooms=addform.number_of_bathrooms.data,
                property_type=addform.property_type.data
            )

            db.session.add(property)
            db.session.commit()
            flash('Property Added', 'success')
            return redirect(url_for('home')) # to be updated to show properties
    return render_template('new_property.html', form=addform)

@app.route('/properties/create/<filename>')
def get_uploaded_file(filename):
    # root_dir = os.getcwd()
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

@app.route('/properties/<propertyid>', methods=['GET','POST'])
def propertyid(propertyid):
    property = db.session.execute(db.select(Property)).filter_by(id=propertyid).scalar_one()
    print(str(property))
    return render_template('property.html', property=property)

def get_uploaded_images():
    file_names = []
    rootdir = os.getcwd()

    for subdir, dirs, files in os.walk(rootdir + app.config['UPLOAD_FOLDER']):
            for file in files:
                filenames_lst = os.path.join(subdir,file)
                file_names.append(os.path.basename(filenames_lst))
    return file_names

###
# The functions below should be applicable to all Flask apps.
###

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
