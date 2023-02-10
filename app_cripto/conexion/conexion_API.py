import requests
from config import *

class Conexion_API:
    def __init__(self, method, url, data = []):
        if method == "GET": #esto es el get al api por si falla al hacer la llamada
            self.call = requests.get(url)
        elif method == "POST":
            self.call = requests.post(url, data)
        else:
            return "ERROR"
        self.call = requests.get(url)
        self.result = self.call.json()
        self.status_code = self.call.status_code
        self.headers = self.call.headers
