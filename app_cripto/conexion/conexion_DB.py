import sqlite3
from config import *

class Conexion_DB:
    def __init__(self, querySql, registro = []):

        self.con = sqlite3.connect(ORIGIN_DATA)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySql, registro)
