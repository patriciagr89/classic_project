from config import *
from app_cripto.conexion.conexion_DB import Conexion_DB
from app_cripto.models.models_API import *

def execute_DB(querySql): #para no repetir el comando de la query a la BBDD
    connect = Conexion_DB(querySql)

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

def get_all_movements(): #obtiene los movimientos de bbdd
    data = execute_DB("SELECT id,date,time,coin_from,quantity_from,coin_to,quantity_to FROM movements ORDER BY date DESC, time DESC;")
    return data

def get_recuperado(): #obtiene importe status recuperado
    data = execute_DB("SELECT sum(quantity_to) as recuperado FROM movements WHERE coin_to = 'EUR';")

    recuperado = 0

    if data[0] is not None and data[0]['recuperado'] is not None:
        recuperado = data[0]['recuperado']

    return recuperado

def get_invertido(): #obtiene importe status inversion
    data = execute_DB("SELECT sum(quantity_from) as invertido FROM movements WHERE coin_from = 'EUR';")

    invertido = 0

    if data[0] is not None and data[0]['invertido'] is not None:
        invertido = data[0]['invertido']

    return invertido

def sum_criptos_to(): #total monedas destino
    data = execute_DB("SELECT coin_to, sum(quantity_to) as sum_criptos_to FROM movements WHERE coin_to <> 'EUR' GROUP BY coin_to;")

    return data

def sum_criptos_from(): #total monedas origen
    data = execute_DB("SELECT coin_from, sum(quantity_from) as sum_criptos_from FROM movements WHERE coin_from <> 'EUR' GROUP BY coin_from;")

    return data

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
    data = execute_DB("SELECT idCoin,coinName FROM coins ORDER BY idCoin;")

    return data