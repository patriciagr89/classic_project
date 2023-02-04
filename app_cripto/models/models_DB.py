import sqlite3
from config import *
from app_cripto.conexion.conexion_DB import Conexion_DB

def insert(registro): #para guardar en la bbdd al pulsar el boton de buy
    connect = Conexion_DB("insert into movements(date,time,coin_from,quantity_from,coin_to,quantity_to) values(?,?,?,?,?,?)", registro)
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

def select_value():
    # SELECT coin_to, sum(quantity_to) as quantity_to FROM movements WHERE coin_to <> "EUR" GROUP BY coin_to;
    # SELECT coin_from, sum(quantity_from) as quantity_from FROM movements WHERE coin_from <> "EUR" GROUP BY coin_from;
    pass

def select_all():
    connect = Conexion_DB("SELECT id,date,time,coin_from,quantity_from,coin_to,quantity_to FROM movements ORDER BY date;")

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

def select_coins_from():
    connect = Conexion_DB("SELECT DISTINCT coin_from FROM movements ORDER BY id;")

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

def select_coins_to():
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