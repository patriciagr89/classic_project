import requests
from config import *

class CoinApi:
    def __init__(self, APIKEY, coin_from, coin_to):
        self.coin_from = coin_from
        self.coin_to = coin_to
        self.rate = None
        self.time = None
        self.url = "https://rest.coinapi.io/v1/exchangerate/{coin_from}/{coin_to}?&apikey={APIKEY}"
        self.result = requests.get(self.url)

    def coinChange(self):
        self.result = self.result.json()
        if self.result.status_code == 200:
            self.rate = self.result['rate']
            self.time = self.result['time']
        else:    
            return "Error"
