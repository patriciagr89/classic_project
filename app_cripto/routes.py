from app_cripto import app
from flask import Flask, flash, redirect, render_template, request, url_for
from app_cripto.models.models_DB import *
from app_cripto.models.models_API import *
from config import *
from datetime import datetime
from app_cripto.forms import MyForm
        

@app.route("/")
def index():
    return render_template("index.html", title = "Tradue tu plataforma de criptomonedas de confianza", isIndex = True)

@app.route("/history")
def history():
    registros = select_all()
    return render_template("history.html", movements = registros, title = "Historial de movimientos realizados", isHistory = True)

@app.route("/disclosures")
def disclosures():
    return render_template("disclosures.html", title = "Menciones legales para clientes de Tradue")

@app.route("/purchase", methods = ["POST","GET"])
def purchase():

    form = MyForm(request.form)

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
        return render_template("purchase.html", form = form, list_request={}, title = "Compre y venda criptomonedas en cuestión de minutos", isPurchase = True)
    else: 
        if "calculate" in request.form:
            list_request = {
                "coin_from": form.coin_from.data,
                "coin_to": form.coin_to.data,
                "quantity_from": form.quantity_from.data
              }

            if form.coin_from.data != form.coin_to.data:
                for item in balances:
                    if float(form.quantity_from.data) > 0.0 and "EUR" == form.coin_from.data or (item["cripto"] == form.coin_from.data and item["balance"] >= form.quantity_from.data):
                        response_api = exchangeRate(form.coin_from.data, form.coin_to.data)
                        quantity_from = float(form.quantity_from.data)
                        quantity_to = float(quantity_from) * float(response_api["rate"])

                        list_request["quantity_to"] = float(quantity_to)
                        list_request["value_unit"] = float(response_api["rate"])

                        return render_template("purchase.html", form = form, list_request = list_request, title = "Compre y venda criptomonedas en cuestión de minutos", isPurchase = True)
                    else:

                        form.validate_on_submit()
                        return render_template("purchase.html", form = form, msgError={}, list_request=list_request, title = "Compre y venda criptomonedas en cuestión de minutos", isPurchase = True)
            else:
                form.validate_on_submit()
                return render_template("purchase.html", form = form, msgError={}, list_request=list_request, title = "Compre y venda criptomonedas en cuestión de minutos", isPurchase = True)
        #nos queda pendiente mostrar error de quantity_from no tienes suficientes monedas para vender 

        if "buy" in request.form:
            list_request = {
                        "coin_from":form.coin_from.data,
                        "coin_to":form.coin_to.data,
                        "quantity_from":form.quantity_from.data,
                        "quantity_to":"",
                        "value_unit":""
                    }
            if form.validate_on_submit():
                now = datetime.now()
                
                insert([now.strftime("%Y-%m-%d"),
                        now.strftime("%H:%M:%S"),
                        form.coin_from.data,
                        form.quantity_from.data,
                        form.coin_to.data,
                        form.quantity_to.data])

                flash("¡Su transacción ha sido realizada correctamente!")
                return redirect(url_for('history'))
            else:
                return render_template("purchase.html", msgError={}, form = form, list_request = list_request, title = "Compre y venda criptomonedas en cuestión de minutos", isPurchase = True)

@app.route("/status")
def status():

    status = select_status()
    current_value = current_total_value()

    return render_template("status.html", status = status, value = current_value, title = "Controle el estado de su inversión", isStatus = True, result = 0)