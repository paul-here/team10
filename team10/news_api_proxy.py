from flask import Flask, request, render_template
from newsapi.newsapi_client import NewsApiClient


###############################
### News API Sample Code
# https://github.com/mattlisiv/newsapi-python/tree/master/newsapi

app = Flask(__name__)


class News:

    def __init__(q):
        newsapi = NewsApiClient(api_key='00d22965bc8847a692f7689dd668ca3c')
        self.query = q


    def get_data():
        return newsapi.get_top_headlines(q=query, language='en')


    def new_query(q):
        self.query = q
        return get_data()


# default route -- homepage
@app.route('/')
def news():
    return render_template('newsapi.html', data=top_headlines)


if __name__ == "__main__":

    app.run(debug=True)
# print(top_headlines)
# news()
