# Name: News_API_Proxy.py`
# Group Members: Chris Mayers, Paul Whipp, Chuy Gomez, David Gin
# Date: 5/12/2019
# Class: CST 205
# Description:  Defines a class which interacts with the newsapi client pass
#               data to the news page template

from flask import request
from newsapi import NewsApiClient

class News:

    def __init__(self, q):
        self.newsapi = NewsApiClient(api_key='00d22965bc8847a692f7689dd668ca3c')
        self.query = q


    def get_data(self):
        return self.newsapi.get_top_headlines(q=self.query, language='en')


    def new_query(self, q):
        self.query = q
        return get_data()
