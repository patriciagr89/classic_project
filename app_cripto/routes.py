from app_cripto import app
from flask import Flask, render_template, request
from app_cripto.models import *

@app.route("/")
def index():
    registros = select_all()
    return render_template("index.html", movements = registros, title = "App Criptomonedas", isIndex = True)

@app.route("/purchase", methods = ["POST","GET"])
def purchase():
    coins_from = select_coins_from()
    coins_to = select_coins_to()
    # consulktwQApi = getApi(apikey, coniuf, voint)
    # consulktwQApi.time
    # consulktwQApi.rate
    return render_template("purchase.html", coins = coins_to, movements = coins_from, title = "Compra/Venta/Tradeo", isPurchase = True)

@app.route("/status")
def status():
    status = select_status()
    return render_template("status.html", movements = status, title = "Estado de la inversión", isStatus = True, result = 0)


