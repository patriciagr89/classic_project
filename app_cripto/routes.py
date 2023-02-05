from app_cripto import app
from flask import Flask, flash, redirect, render_template, request, url_for
from app_cripto.models.models_DB import *
from app_cripto.models.models_API import *
from config import *
from datetime import datetime

@app.route("/")
def index():
    registros = select_all()
    return render_template("index.html", movements = registros, title = "Tu plataforma de criptomonedas de confianza", isIndex = True)

@app.route("/purchase", methods = ["POST","GET"])
def purchase():

    coins_from = get_balance()
    coins_to = select_list_coins_to()

    if request.method == "GET": #esto es el get de la llamada a mi purchase que no es lo mismo que mi get de la llamada a la api
        return render_template("purchase.html", form = None, list_to = coins_to, list_from = coins_from, title = "Compra/Venta/Tradeo", isPurchase = True)

    else: 
        if "calculate" in request.form:
            
            response_api = exchangeRate(request.form["coin_from"], request.form["coin_to"])
            quantity_from = float(request.form["quantity_from"])
            quantity_to = float(quantity_from * response_api["rate"])

            list_request = {
                    "coin_from":request.form["coin_from"],
                    "coin_to":request.form["coin_to"],
                    "quantity_from":request.form["quantity_from"],
                    "quantity_to":str(quantity_to),
                    "value_unit":str(response_api["rate"]),
                    "time":str(response_api["time"])
                }

            return render_template("purchase.html", form = list_request, list_to = coins_to, list_from = coins_from, title = "Compra y venta de monedas", isPurchase = True)

        if "buy" in request.form:
            
            now = datetime.now()
            
            insert([now.strftime("%Y-%m-%d"),
                    now.strftime("%H:%M:%S"),
                    request.form["coin_from"],
                    request.form["quantity_from"],
                    request.form["coin_to"],
                    request.form["quantity_to"]])

            flash("¡Transacción realizada correctamente!")
            return redirect(url_for('index'))

@app.route("/status")
def status():

    status = select_status()
    current_value = current_total_value()

    return render_template("status.html", status = status, value = current_value, title = "Estado de la inversión", isStatus = True, result = 0)
