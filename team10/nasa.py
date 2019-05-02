from flask import Flask, render_template 
from flask_bootstrap import Bootstrap
from PIL import Image
import os, sys
import random
import requests, json
from pprint import pprint


#key: cGzGzKqlSZgxF9T7ld9L2KDXEZlCuJdFfNyDyLKD


endpoint = 'https://api.nasa.gov/planetary/apod?api_key=cGzGzKqlSZgxF9T7ld9L2KDXEZlCuJdFfNyDyLKD&hd=true'





try:
    r = requests.get(endpoint)
    data = r.json()
    pprint(data)

    url = data['hdurl']
    explanation = data['explanation']

except:
    print('please try again')


# create an instance of the Flask class
app = Flask(__name__, static_url_path = "/static", static_folder = "static")
bootstrap = Bootstrap(app)

# route() decorator binds a function to a URL
@app.route('/nasa')
def index():

	return render_template('nasa.html', link=url, words=explanation)