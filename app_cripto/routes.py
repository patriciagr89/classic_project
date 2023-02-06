from app_cripto import app
from flask import Flask, flash, redirect, render_template, request, url_for
from app_cripto.models.models_DB import *
from app_cripto.models.models_API import *
from config import *
from datetime import datetime
from app_cripto.forms import MyForm

@app.route("/")
def index():
    registros = select_all()
    return render_template("index.html", movements = registros, title = "Tu plataforma de criptomonedas de confianza", isIndex = True)

@app.route("/purchase", methods = ["POST","GET"])
def purchase():

    form = MyForm()

    balances = get_balance()
    coins_from = ["EUR"]
    for balance in balances:
        if balance["balance"] > 0:
            coins_from.append(balance["cripto"])
    form.coin_from.choices = coins_from

    coins_to_objets = select_list_coins_to()
    coins_to = []
    for coin in coins_to_objets:
        coins_to.append(coin["coinName"])
    form.coin_to.choices = coins_to

    if request.method == "GET": #esto es el get de la llamada a mi purchase que no es lo mismo que mi get de la llamada a la api
        return render_template("purchase.html", form = form, list_request = {}, title = "Compra y venta de monedas", isPurchase = True)
    else: 
        if "calculate" in request.form:
            response_api = exchangeRate(form.coin_from.data, form.coin_to.data)
            quantity_from = float(form.quantity_from.data)
            quantity_to = float(quantity_from * response_api["rate"])

            list_request = {
                        "coin_from":form.coin_from.data,
                        "coin_to":form.coin_to.data,
                        "quantity_from":form.quantity_from.data,
                        "quantity_to":str(quantity_to),
                        "value_unit":str(response_api["rate"])
                    }

            return render_template("purchase.html", form = form, list_request = list_request, title = "Compra y venta de monedas", isPurchase = True)
        
        if "buy" in request.form:
            if form.validate_on_submit():
                now = datetime.now()
                
                insert([now.strftime("%Y-%m-%d"),
                        now.strftime("%H:%M:%S"),
                        form.coin_from.data,
                        form.quantity_from.data,
                        form.coin_to.data,
                        form.quantity_to.data])

                flash("¡Transacción realizada correctamente!")
                return redirect(url_for('index'))
            else:
                return render_template("purchase.html", msgError={}, form = form, list_request = {}, title = "Compra y venta de monedas", isPurchase = True)

@app.route("/status")
def status():

    status = select_status()
    current_value = current_total_value()

    return render_template("status.html", status = status, value = current_value, title = "Estado de la inversión", isStatus = True, result = 0)
