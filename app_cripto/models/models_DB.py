from config import *
from app_cripto.conexion.conexion_DB import Conexion_DB
from app_cripto.models.models_API import *


def get_all_movements(): #obtenemos los movimientos de bbdd
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

def insert_movement(registro): #guarda los datos introducidos en mi bbdd al pulsar boton buy
    connect = Conexion_DB("INSERT INTO movements(date,time,coin_from,quantity_from,coin_to,quantity_to) values(?,?,?,?,?,?)", registro)
    connect.con.commit()
    connect.con.close()

def get_status(): #obtiene importe inversion y recuperado
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

    status = resultado[0]

    if status is not None and (status['invertido'] is None or status['recuperado'] is None):
        status = None

    return status

def sum_criptos_to(): #total monedas destino
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

def sum_criptos_from(): #total monedas origen
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

def get_balance(): #obtiene el saldo total de cada moneda restando monedas destino menos monedas origen
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

def select_list_coins_to(): #obtiene listado de las monedas destino

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