from flask import Flask, render_template
from PIL import Image
from random import *
import requests, json
from pprint import pprint

app = Flask(__name__)

joke = "yeet"

im = "yote"

endpoint = 'https://api.chucknorris.io/jokes/random'

try:
    r = requests.get(endpoint)
    data = r.json()
    
    joke = data["value"]
    im = data["icon_url"]
    
except:
    print('please try again')

@app.route('/')
def home():
    return render_template('chuck.html', joke2=joke, im2=im)

if __name__=='__main__':
        app.run(debug=True)
