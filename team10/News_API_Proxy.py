from flask import Flask, request, render_template
from newsapi.newsapi_client import NewsApiClient

###############################
### News API Sample Code
# https://github.com/mattlisiv/newsapi-python/tree/master/newsapi

class News:

    def __init__(self, q):
        self.newsapi = NewsApiClient(api_key='00d22965bc8847a692f7689dd668ca3c')
        self.query = q


    def get_data(self):
        return self.newsapi.get_top_headlines(q=self.query, language='en')


    def new_query(self, q):
        self.query = q
        return get_data()


# # default route -- homepage
# @app.route('/')
# def news():
#     return render_template('newsapi.html', data=news.get_data())


# if __name__ == "__main__":
#     app = Flask(__name__)
#     news = News('bitcoin')
#     app.run(debug=True)
