from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

class Search(FlaskForm):
    query = StringField('Search for news: ', validators=[DataRequired()])
    submit = SubmitField('Submit')
