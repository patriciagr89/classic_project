import sqlite3
from config import *
from app_cripto.conexion.conexion_API import Conexion_API

# def exchangeRate(coin_from, coin_to): #para guardar en la bbdd al pulsar el boton de buy
#     print("llamo api")
#     resultCall = Conexion_API("GET", f"https://rest.coinapi.io/v1/exchangerate/{coin_from}/{coin_to}?&apikey={APIKEY}")
#     if resultCall.status_code == 200:
#         return resultCall.result
#     if resultCall.status_code == 429:
#         return "Has gastado todas tus llamadas al api"
#     else:    
#         return "Error"

def exchangeRate(coin_from, coin_to):  #aqui he mockeado la api cuando el limite de peticiones se ha excedido de 100 al día
    print("llamo api")
    mock_api = {
        "time":"2023-01-31T20:21:18.0000000Z",
        "asset_id_base":"EUR",
        "asset_id_quote": "BTC",
        "rate": 0.0000469827
    }
    return mock_api
