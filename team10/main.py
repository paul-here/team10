from flask import Flask, request, render_template
from News_API_Proxy import News


# init objects
app = Flask(__name__)


# default route -- homepage
@app.route('/')
def default():
    return render_template('homepage.html')


@app.route('/news')
def news():
    news_proxy = News('bitcoin')
    return render_template('newsapi.html', data=news_proxy.get_data())

if __name__ == "__main__":
    app.run(debug=True)
