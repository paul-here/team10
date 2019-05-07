from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

class Search(FlaskForm):
    query = StringField('Query', validators=[DataRequired()])
    submit = SubmitField('Submit')
