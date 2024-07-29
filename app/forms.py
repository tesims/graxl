from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, FileField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class DashboardForm(FlaskForm):
    project_name = StringField('Project Name', validators=[DataRequired()])
    sector = StringField('Sector', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    faces = BooleanField('Video + Images: face, full-body, tattoos, logos, location')
    text = BooleanField('Audio + Text: name, location, race, gender, age')
    prompt = TextAreaField('Prompt', validators=[DataRequired()])
    audio = FileField('Upload Unmasked Audio')
    text = TextAreaField('Insert Unmasked Text')
    image = FileField('Upload Unmasked Image')
    video = FileField('Upload Unmasked Video', validators=[DataRequired()])
    terms = BooleanField('I have read and accept the terms and conditions', validators=[DataRequired()])
    submit = SubmitField('Submit')