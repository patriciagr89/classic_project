import sqlite3
from config import *
from app_cripto.conexion.conexion_API import Conexion_API

def exchangeRate(coin_from, coin_to): #para guardar en la bbdd al pulsar el boton de buy
    resultCall = Conexion_API("GET", f"https://rest.coinapi.io/v1/exchangerate/{coin_from}/{coin_to}?&apikey={APIKEY}")
    if resultCall.status_code == 200:
        return resultCall.result
    else:    
        return "Error"
