from flask import Flask, request, render_template, redirect
from .News_API_Proxy import News
from .Search_Form import Search
from .Weather_API_Proxy import Weather
from .NASA_API_Proxy import NASA

# init app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'

# default route -- homepage
@app.route('/')
def default():
    return render_template('homepage.html', iframe_src="/search")

# News search bar
@app.route('/search', methods = ['POST', 'GET'])
def search():
    form = Search()
    if form.validate_on_submit():
        return redirect('/news/' + str(form.query.data))
    return render_template('searchbar.html', form=form)

# Relevant news
@app.route('/news/<q>')
def news(q):
    if q == "":
        return redirect('/search')
    news_proxy = News(q)
    return render_template('newsapi.html', data=news_proxy.get_data())

# Weather in Monterey
@app.route('/weather')
def weather():
	weather_proxy = Weather()
	return render_template('weather.html', city=weather_proxy.get_city(),
            temp=weather_proxy.get_temp(), conditions=weather_proxy.get_cond(),
            wind=weather_proxy.get_wind(), pressure=weather_proxy.get_pres(),
            humid=weather_proxy.get_humi(), graphic=weather_proxy.get_grap())

# NASA image of the day
@app.route('/nasa')
def nasa():
	nasa = NASA()
	return render_template('nasa.html', words=nasa.get_desc(), link=nasa.get_url())

# Google redirect
@app.route('/goog')
def goog():
    return redirect('https://www.google.com/search?igu=1')

if __name__ == "__main__":
    app.run(debug=True)
