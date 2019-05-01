from flask import Flask, render_template 
from flask_bootstrap import Bootstrap
from PIL import Image
import os, sys
import random
import requests, json
from pprint import pprint



endpoint = 'https://www.metaweather.com/api/location/2488853'

city_name = "Monterey"
current_conditions = ""
current_temp = ""
wind_speed = ""
air_pressure = ""
humidity = ""


try:
    r = requests.get(endpoint)
    data = r.json()
    pprint(data)

    condition_abbr = data['consolidated_weather'][0]['weather_state_abbr']
    current_conditions = data['consolidated_weather'][0]["weather_state_name"]
    current_temp = data['consolidated_weather'][0]['the_temp']
    wind_speed = data['consolidated_weather'][0]['wind_speed']
    air_pressure = data['consolidated_weather'][0]['air_pressure']
    humidity = data['consolidated_weather'][0]['humidity']

    if condition_abbr == "sn":
    	graphic_link = "/static/img/weather/png/sn.png"
    if condition_abbr == "sl":
    	graphic_link = "/static/img/weather/png/sl.png"
    if condition_abbr == "h":
    	graphic_link = "/static/img/weather/png/h.png"
    if condition_abbr == "t":
    	graphic_link = "/static/img/weather/png/t.png"
    if condition_abbr == "hr":
    	graphic_link = "/static/img/weather/png/hr.png"
    if condition_abbr == "lr":
    	graphic_link = "/static/img/weather/png/lr.png"
    if condition_abbr == "s":
    	graphic_link = "/static/img/weather/png/s.png"
    if condition_abbr == "hc":
    	graphic_link = "/static/img/weather/png/hc.png"
    if condition_abbr == "lc":
    	graphic_link = "/static/img/weather/png/lc.png"
    if condition_abbr == "c":
    	graphic_link = "/static/img/weather/png/c.png"

    fTemp = (current_temp * 1.8) + 32

    fTemp = float('%.1f'%(fTemp))

    wind_speed = float('%.1f'%(wind_speed))

    air_pressure =float('%.1f'%(air_pressure))

    print(data['consolidated_weather'][0])
    print("London Weather: ")
    print("Current Conditions:  " + current_conditions)
    print("Current Temperature: " + str(fTemp) + " degrees celsius")
    print("Current Wind:        " + str(wind_speed) + " mph")
    print("Air Pressure:        " + str(air_pressure) + " mbar")
    print("Humidity:            " + str(humidity) + "%")



except:
    print('please try again')


# create an instance of the Flask class
app = Flask(__name__, static_url_path = "/static", static_folder = "static")
bootstrap = Bootstrap(app)

# route() decorator binds a function to a URL
@app.route('/weather')
def index():

	return render_template('index.html', city=city_name, conditions=current_conditions, temp = fTemp, wind=wind_speed, pressure=air_pressure, humid=humidity, graphic=graphic_link)