from config import *
from app_cripto.conexion.conexion_API import Conexion_API

def exchangeRate(coin_from, coin_to): #para guardar en la bbdd al pulsar el boton de buy
    resultCall = Conexion_API("GET", f"https://rest.coinapi.io/v1/exchangerate/{coin_from}/{coin_to}?&apikey={APIKEY}")

    if resultCall.status_code == 200:
        return resultCall.result
    if resultCall.status_code == 429:
        return "Has superado el límite máximo de llamadas al api por día."
    else:
        return "Error"

"""
def exchangeRate(coin_from, coin_to):  #aqui he mockeado la api cuando el limite de peticiones se ha excedido de 100 al día
    mock_api = {
        "time":"2023-01-31T20:21:18.0000000Z",
        "asset_id_base":"EUR",
        "asset_id_quote": "BTC",
        "rate": 0.0000469827
    }

    return mock_api
"""

def exchangeAllCoinsTo(coin_to): #sacamos todos los valores en EUR de las criptos
    print("llamo api")
    resultCall = Conexion_API("GET", f"https://rest.coinapi.io/v1/exchangerate/{coin_to}?apikey={APIKEY}")
    if resultCall.status_code == 200:
        result = []
        if resultCall.result is not None and resultCall.result["rates"] is not None:
            result = resultCall.result["rates"]
        return result
    if resultCall.status_code == 429:
        return "Has superado el límite máximo de llamadas al api por día."
    else:    
        return "Error"
