from flask import Flask, request, render_template
from newsapi.newsapi_client import NewsApiClient


###############################
### News API Sample Code

# https://github.com/mattlisiv/newsapi-python/tree/master/newsapi <-- more info

# Init
newsapi = NewsApiClient(api_key='00d22965bc8847a692f7689dd668ca3c')
app = Flask(__name__)
# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin', language='en')
                                          #sources='bbc-news,the-verge',
                                          #category='business',
                                          #language='en'
                                          #country='us')
#
# # /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)
#
# # /v2/sources
# sources = newsapi.get_sources()


# default route -- homepage
@app.route('/')
def news():
    return render_template('newsapi.html', data=top_headlines)


if __name__ == "__main__":
    app.run(debug=True)
# print(top_headlines)
# news()
