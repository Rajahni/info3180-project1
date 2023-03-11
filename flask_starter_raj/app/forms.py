from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Email
from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os

csrf = CSRFProtect()

app = Flask('__name__', template_folder="app/templates/")
app.config['SECRET_KEY'] = 'SomeSecretKey'
csrf.init_app(app)

class AddForm(FlaskForm):
    proptitle = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    norooms = StringField('No. of Rooms', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(),
            FileAllowed(['jpg', 'jpeg', 'png'], 'Images Only!')
    ])
    bathrooms = StringField('no. of Bathrooms', validators=[InputRequired()])
    proptype = SelectField('Property Type', choices=[('house', 'House'), ('apartment', 'Apartment')])

