import os, sys
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