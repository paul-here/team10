from flask import Flask, request, render_template, redirect
from News_API_Proxy import News
from Search_Form import Search

# init app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
#global query

# default route -- homepage
@app.route('/')
def default():
    return render_template('homepage.html', iframe_src="/search")


@app.route('/search', methods = ['POST', 'GET'])
def search():
    form = Search()
    if form.validate_on_submit():
        return redirect('/news/' + str(form.query.data))
    return render_template('searchbar.html', form=form)


@app.route('/news/<q>')
def news(q):
    if q == "":
        return redirect('/search')
    news_proxy = News(q)
    return render_template('newsapi.html', data=news_proxy.get_data())


if __name__ == "__main__":
    app.run(debug=True)
