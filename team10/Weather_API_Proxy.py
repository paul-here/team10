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
			if condition_abbr == "sn":
				self.graphic_link = "/static/img/weather/png/sn.png"
			if condition_abbr == "sl":
				self.graphic_link = "/static/img/weather/png/sl.png"
			if condition_abbr == "h":
				self.graphic_link = "/static/img/weather/png/h.png"
			if condition_abbr == "t":
				self.graphic_link = "/static/img/weather/png/t.png"
			if condition_abbr == "hr":
				self.graphic_link = "/static/img/weather/png/hr.png"
			if condition_abbr == "lr":
				self.graphic_link = "/static/img/weather/png/lr.png"
			if condition_abbr == "s":
				self.graphic_link = "/static/img/weather/png/s.png"
			if condition_abbr == "hc":
				self.graphic_link = "/static/img/weather/png/hc.png"
			if condition_abbr == "lc":
				self.graphic_link = "/static/img/weather/png/lc.png"
			if condition_abbr == "c":
				self.graphic_link = "/static/img/weather/png/c.png"
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