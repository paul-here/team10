from flask import Flask, request, render_template
from News_API_Proxy import News


# init app
app = Flask(__name__)

# default route -- homepage
@app.route('/')
def default():
    return render_template('homepage.html', iframe_src="/news")


@app.route('/news')
def news():
    # init proxy
    query = request.args.get('query', default = "")
    if(query == ""):
        return render_template('searchbar.html')
    else:
        news_proxy = News('bitcoin')
        return render_template('newsapi.html', data=news_proxy.get_data())

if __name__ == "__main__":
    app.run(debug=True)
