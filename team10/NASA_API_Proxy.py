# Name: NASA_API_Proxy.py
# Group Members: Chris Mayers, Paul Whipp, Chuy Gomez, David Gin
# Date: 5/12/2019
# Class: CST 205
# Description: 	Defines a class which interacts with the NASA API to pass data
# 				to the nasa image page template

import requests, json

class NASA:

	def __init__(self):

		endpoint = 'https://api.nasa.gov/planetary/apod?api_key=cGzGzKqlSZgxF9T7ld9L2KDXEZlCuJdFfNyDyLKD&hd=true'

		try:
			r = requests.get(endpoint)
			data = r.json()
			self.url = data['url']
			self.desc = data['explanation']

		except:
			print('please try again')

	def get_url(self):
		return self.url

	def get_desc(self):
		return self.desc
