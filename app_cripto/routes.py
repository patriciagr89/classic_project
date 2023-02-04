from app_cripto import app
from flask import Flask, render_template, request
from app_cripto.models.models_DB import *
from app_cripto.models.models_API import *
from config import *

@app.route("/")
def index():
    registros = select_all()
    return render_template("index.html", movements = registros, title = "App Criptomonedas", isIndex = True)

@app.route("/purchase", methods = ["POST","GET"])
def purchase():

    coins_from = select_coins_from()
    coins_to = select_coins_to()

    if request.method == "GET": #esto es el get de la llamada a mi purchase que no es lo mismo que mi get de la llamada a la api
        return render_template("purchase.html", form = None, coins = coins_to, movements = coins_from, title = "Compra/Venta/Tradeo", isPurchase = True)

    else: 
        if "calculate" in request.form:
            response_api = exchangeRate(request.form["coins_from"], request.form["coins_to"])
            quantity_from = float(request.form["quantity_from"])
            quantity_to = float(quantity_from * response_api["rate"])

            list_request = {
                    "coins_from":request.form["coins_from"],
                    "coins_to":request.form["coins_to"],
                    "quantity_from":request.form["quantity_from"],
                    "quantity_to":str(quantity_to),
                    "value_unit":str(response_api["rate"]),
                    "time":str(response_api["time"])
                }

            return render_template("purchase.html", form = list_request, coins = coins_to, movements = coins_from, title = "Compra/Venta/Tradeo", isPurchase = True)

        if "buy" in request.form:
            return "Aqui guardamos en sqlite"

@app.route("/status")
def status():
    status = select_status()
    return render_template("status.html", movements = status, title = "Estado de la inversión", isStatus = True, result = 0)
