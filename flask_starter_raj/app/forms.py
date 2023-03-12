from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, IntegerField
from wtforms.validators import InputRequired, Email
from flask import Flask
import os

class AddForm(FlaskForm):
    proptitle = StringField('Property Title', validators=[InputRequired()])

    description = TextAreaField('Description', validators=[InputRequired()])

    number_of_rooms = IntegerField('No. of Rooms', validators=[InputRequired()])

    price = IntegerField('Price', validators=[InputRequired()])

    location = StringField('Location', validators=[InputRequired()])

    photo = FileField('Photo', validators=[FileRequired(),
            FileAllowed(['jpg', 'jpeg', 'png'], 'Images Only!')
    ])
    number_of_bathrooms = IntegerField('no. of Bathrooms', validators=[InputRequired()])

    property_type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])

