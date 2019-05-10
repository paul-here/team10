from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PIL import Image
import os, sys
import random
import requests, json
from pprint import pprint

class Weather:

	def __init__(self):

		self.endpoint = 'https://www.metaweather.com/api/location/2488853'
		self.city_name = "Monterey"
		current_temp = ""
		wind_speed = ""
		air_pressure = ""
		humidity = ""

		try:
			r = requests.get(self.endpoint)
			data = r.json()

			condition_abbr = data['consolidated_weather'][0]['weather_state_abbr']
			self.current_conditions = data['consolidated_weather'][0]["weather_state_name"]
			current_temp = data['consolidated_weather'][0]['the_temp']
			wind_speed = data['consolidated_weather'][0]['wind_speed']
			air_pressure = data['consolidated_weather'][0]['air_pressure']
			self.humidity = data['consolidated_weather'][0]['humidity']
			self.graphic_link = "/static/img/weather/" + condition_abbr + ".png"
			holdFTemp = (current_temp * 1.8) + 32
			self.fTemp = float('%.1f'%(holdFTemp))
			self.wind_speed = float('%.1f'%(wind_speed))
			self.aPressure =float('%.1f'%(air_pressure))

		except:
			print('please try again')


	def get_city(self):
		return self.city_name

	def get_temp(self):
		return self.fTemp

	def get_cond(self):
		return self.current_conditions

	def get_humi(self):
		return self.humidity

	def get_grap(self):
		return self.graphic_link

	def get_wind(self):
		return self.wind_speed

	def get_pres(self):
		return self.aPressure
