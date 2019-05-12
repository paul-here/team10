# Name: Chuck_API_Proxy
# Group Members: Chris Mayers, Paul Whipp, Chuy Gomez, David Gin
# Date: 5/10/2019
# Class: CST 205
# Description: Defines a class which interacts with the Chuck API to pass data to main homepage page template
import requests, json

class Chuck:
    
    def __init__(self):
        
        endpoint = 'https://api.chucknorris.io/jokes/random'

        try:
            r = requests.get(endpoint)
            data = r.json()
            self.joke = data["value"]
            self.im = data["icon_url"]

        except:
            print('please try again')

    def get_joke(self):
        return self.joke
    
    def get_im(self):
        return self.im
