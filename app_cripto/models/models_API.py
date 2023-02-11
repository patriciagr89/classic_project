from config import *
from app_cripto.conexion.conexion_API import Conexion_API
from flask import flash

def exchangeRate(coin_from, coin_to): #obtiene equivalencia de una moneda en otra
    resultCall = Conexion_API("GET", f"https://rest.coinapi.io/v1/exchangerate/{coin_from}/{coin_to}?&apikey={APIKEY}")

    if resultCall.status_code == 200:
        return resultCall
    if resultCall.status_code == 429:
        flash("¡Imposible realizar su transacción, se ha superado el límite máximo de 100 llamadas al api por día!")
        return None
    else:
        flash("¡Se ha producido un error!")
        return None

def exchangeAllCoinsTo(coin_to): #obtiene todos los valores en EUR de todas las criptos
    print("llamo api exchangeAllCoinsTo")
    resultCall = Conexion_API("GET", f"https://rest.coinapi.io/v1/exchangerate/{coin_to}?apikey={APIKEY}")
    if resultCall.status_code == 200:
        return resultCall
    if resultCall.status_code == 429:
        flash("¡Imposible calcular su estado finaciero, se ha superado el límite máximo de 100 llamadas al api por día!")
        return None
    else:
        flash("¡Se ha producido un error!")
        return None