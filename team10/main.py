from flask import Flask, request, render_template
from News_API_Proxy import News
from Search_Form import Search

# init app
app = Flask(__name__)
query = ""

# default route -- homepage
@app.route('/')
def default():
    return render_template('homepage.html', iframe_src="/news")


@app.route('/search', methods = ['POST', 'GET'])
def search():
    form = Search()
    if form.validate_on_submit():
        query = form.query.data
        return redirect('/news')


@app.route('/news')
def news():
    if query == "":
        return redirect('/search')
    news_proxy = News(query)
    return render_template('newsapi.html', data=news_proxy.get_data())


if __name__ == "__main__":
    app.run(debug=True)
