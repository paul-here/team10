# Name: Search_Form.py
# Group Members: Chris Mayers, Paul Whipp, Chuy Gomez, David Gin
# Date: 5/12/2019
# Class: CST 205
# Description:  Defines a class which interacts with the search bar in order to
#               validate and return a search query

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

class Search(FlaskForm):
    query = StringField('Search for news: ', validators=[DataRequired()])
    submit = SubmitField('Submit')
