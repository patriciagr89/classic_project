import requests
from config import *

"""class CallApi:
    def __init__(self, coin_from, coin_to):
        self.coin_from = coin_from
        self.coin_to = coin_to
        self.rate = None
        self.time = None
        self.result = None

    def coinChange(self, APIKEY):
        self.result = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{self.coin_from}/{self.coin_to}?&apikey={APIKEY}")
        if self.result.status_code == 200:
            self.result = self.result.json()
            self.rate = self.result['rate']
            self.time = self.result['time']
        else:    
            return "Error"
"""


class CallApi:
    def __init__(self, coin_from, coin_to):
        self.coin_from = coin_from
        self.coin_to = coin_to
        self.call = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{self.coin_from}/{self.coin_to}?&apikey={APIKEY}")
        self.result = self.call.json()
        self.rate = self.result['rate']
        self.time = self.result['time']
