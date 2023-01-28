from app_cripto import app
from flask import Flask, render_template, request
from app_cripto.models import *

@app.route("/")
def index():
    registros = select_all()
    return render_template("index.html", movements = registros, title = "App Criptomonedas", isIndex = True)

@app.route("/purchase", methods = ["POST","GET"])
def purchase():
    coinslist = select_coins()
    return render_template("purchase.html", coins = coinslist, title = "Compra/Venta/Tradeo", isPurchase = True)

@app.route("/status")
def status():
    status = select_status()
    return render_template("status.html", movements = status, title = "Estado de la inversión", isStatus = True, result = 0)

