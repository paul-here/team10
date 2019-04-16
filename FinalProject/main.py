from flask import Flask, request, render_template

# dexterrules.com
# Passing __name__ helps it "find the root path"? what
app = Flask(__name__)


@app.route('/gallery')
def gallery():
    return render_template('homepage.html')

@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/resume')
def resume():
    return render_template('DexterGallery.html')


@app.route('/blog')
def blog():
    return '<h>this is my blog</h>'


if __name__ == "__main__":
    app.run(debug=True)


# 3/16/2019 -- CST 205 -- Lab 13 -- Beautiful Soup Web Scraping
# By Michael Avalos-Garcia, Jesus Andres Bernal, and Paul Whipp
# Description: This program creates a headless Mozilla browser, converts the
#              HTML DOM into a BeautifulSoup object, and then searches for all
#              images and prints their URLs

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# My website from CST 336
my_site = 'http://pwhipp-cst336.herokuapp.com/labs/lab1/'
# package up request info
req = Request(
    my_site,
    headers={'User-Agent': 'Mozilla/5.0'}
)
# make request, convert to BeautifulSoup object
resp = urlopen(req)
bs_obj = BeautifulSoup(resp.read(), 'lxml')
# search bs_obj
for link in bs_obj.findAll("img"):
    if 'src' in link.attrs:
        print(link.attrs['src'])
