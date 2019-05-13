# Project: There's No Page Like Homepage
# Project Description:  A simple homepage with searchable news, quick access to
#                       google, a quick laugh, or the weather.
# Name: main.py
# Group Members: Chris Mayers, Paul Whipp, Chuy Gomez, David Gin
# Date: 5/12/2019
# Class: CST 205
# Description:  This script creates a Flask server and coordinates the
#               interaction between the API objects and the website.


from flask import Flask, request, render_template, redirect
from News_API_Proxy import News
from Search_Form import Search
from Weather_API_Proxy import Weather
from NASA_API_Proxy import NASA
from Chuck_API_proxy import Chuck

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

# Chuck Norris Joke
@app.route('/chuck')
def chuck():
    chuck = Chuck()
    return render_template('chuck.html', joke=chuck.get_joke(), im=chuck.get_im())

# Google redirect
@app.route('/goog')
def goog():
    return redirect('https://www.google.com/search?igu=1')

# run app
if __name__ == "__main__":
    app.run(debug=True)
