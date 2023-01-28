import sqlite3
from config import *
from app_cripto.conexion import Conexion

def select_status():
    connect = Conexion("SELECT sum(cantidad_from) as invertido, sum(cantidad_to) as recuperado FROM movements WHERE moneda_from = 'EUR';")

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
    # SELECT moneda_to, sum(cantidad_to) as quantity_to FROM movements WHERE moneda_to <> "EUR" GROUP BY moneda_to;
    # SELECT moneda_from, sum(cantidad_from) as quantity_from FROM movements WHERE moneda_from <> "EUR" GROUP BY moneda_from;
    pass

def select_all():
    connect = Conexion("select id,date,time,moneda_from,cantidad_from,moneda_to,cantidad_to from movements order by date;")

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