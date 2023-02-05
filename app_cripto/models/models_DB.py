import sqlite3
from config import *
from app_cripto.conexion.conexion_DB import Conexion_DB
from app_cripto.models.models_API import *

def insert(registro): #para guardar en la bbdd al pulsar el boton de buy
    connect = Conexion_DB("INSERT INTO movements(date,time,coin_from,quantity_from,coin_to,quantity_to) values(?,?,?,?,?,?)", registro)
    connect.con.commit()
    connect.con.close()

def select_status():
    connect = Conexion_DB("SELECT sum(quantity_from) as invertido, sum(quantity_to) as recuperado FROM movements WHERE coin_from = 'EUR';")

    filas = connect.res.fetchall()
    columnas = connect.res.description

    resultado = []

    for fila in filas:
        dato = {}
        posicion = 0

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connect.con.close()
    return resultado[0]

def sum_criptos_to():
    connect = Conexion_DB("SELECT coin_to, sum(quantity_to) as sum_criptos_to FROM movements WHERE coin_to <> 'EUR' GROUP BY coin_to;")

    filas = connect.res.fetchall()
    columnas = connect.res.description

    resultado = []

    for fila in filas:
        dato = {}
        posicion = 0

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connect.con.close()
    return resultado

def sum_criptos_from():
    connect = Conexion_DB("SELECT coin_from, sum(quantity_from) as sum_criptos_from FROM movements WHERE coin_from <> 'EUR' GROUP BY coin_from;")

    filas = connect.res.fetchall()
    columnas = connect.res.description

    resultado = []

    for fila in filas:
        dato = {}
        posicion = 0

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connect.con.close()
    return resultado

def get_balance():
    sum_total = []
    criptos_added = []
    sum_to = sum_criptos_to()
    sum_from = sum_criptos_from()

    for item_to in sum_to:
        for item_from in sum_from:
            if item_to["coin_to"] == item_from["coin_from"]:
                sum_total.append({"cripto": item_to["coin_to"], "balance": item_to["sum_criptos_to"] - item_from["sum_criptos_from"]})
                criptos_added.append(item_to["coin_to"])

        if item_to["coin_to"] not in criptos_added:
            sum_total.append({"cripto": item_to["coin_to"], "balance": item_to["sum_criptos_to"]})

    return sum_total

def current_total_value():
    
    criptos_balance = get_balance()
    sum_criptos_exchange = 0

    for item in criptos_balance:
        if item["balance"] > 0:
            response_api = exchangeRate(item["cripto"], "EUR")
            current_balance = item["balance"] * response_api["rate"]
            sum_criptos_exchange += current_balance

    return  sum_criptos_exchange

def select_all():
    connect = Conexion_DB("SELECT id,date,time,coin_from,quantity_from,coin_to,quantity_to FROM movements ORDER BY date DESC, time DESC;")

    filas = connect.res.fetchall()
    columnas = connect.res.description

    resultado = []

    for fila in filas:
        dato = {}
        posicion = 0

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connect.con.close()
    return resultado

def select_list_coins_to():
    connect = Conexion_DB("SELECT idCoin,coinName FROM coins ORDER BY idCoin;")

    filas = connect.res.fetchall()
    columnas = connect.res.description

    resultado = []

    for fila in filas:
        dato = {}
        posicion = 0

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connect.con.close()
    return resultado