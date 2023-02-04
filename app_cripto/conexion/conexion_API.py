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
        self.call = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{self.coin_from}/{self.coin_to}?&apikey={APIKEY}")
        if self.call.status_code == 200:
            self.result = self.call.json()
            self.rate = self.result['rate']
            self.time = self.result['time']
        else:    
            return "Error"
"""


class Conexion_API:
    def __init__(self, method, url, data = []):
        # self.coin_from = coin_from
        # self.coin_to = coin_to
        if method == "GET": #esto es el get a la api por si falla al hacer la llamada
            self.call = requests.get(url)
        elif method == "POST":
            self.call = requests.post(url, data)
        # elif method == "PUT":
        #     self.call = requests.put(url, data)
        # elif method == "DELETE":
        #     self.call = requests.delete(url, data)
        else:
            return "ERROR"
        self.call = requests.get(url)
        self.result = self.call.json()
        # self.rate = self.result['rate']
        # self.time = self.result['time']
        self.status_code = self.call.status_code
