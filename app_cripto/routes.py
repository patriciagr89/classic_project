from app_cripto import app
from flask import flash, redirect, render_template, request, url_for
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
    registros = get_all_movements()
    return render_template("history.html", movements = registros, title = "Historial de movimientos realizados", isHistory = True)

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

    if request.method == "GET": #esto es el get a purchase
        return render_template("purchase.html", form = form, list_request={}, title = "Compre y venda criptomonedas en cuestión de minutos", isPurchase = True)

    else:
        if "calculate" in request.form:
            list_request = {
                "coin_from": form.coin_from.data,
                "coin_to": form.coin_to.data,
                "quantity_from": form.quantity_from.data
            }

            callExchageRate = False

            if form.coin_from.data != form.coin_to.data:
                if (balances is None or len(balances) < 1) or "EUR" == form.coin_from.data:
                    callExchageRate = "EUR" == form.coin_from.data and float(form.quantity_from.data) > 0.0
                else :
                    for item in balances:
                        if item["cripto"] == form.coin_from.data:
                            if float(form.quantity_from.data) > 0.0 and ("EUR" == form.coin_from.data or item["balance"] >= float(form.quantity_from.data)):
                                callExchageRate = True

            if callExchageRate:
                response_api = exchangeRate(form.coin_from.data, form.coin_to.data)
                if response_api is not None:
                    quantity_from = float(form.quantity_from.data)
                    quantity_to = float(quantity_from) * float(response_api["rate"])

                    list_request["quantity_to"] = float(quantity_to)
                    list_request["value_unit"] = float(response_api["rate"])
            else: 
                form.validate_on_submit()

            return render_template("purchase.html", form = form, msgError={}, list_request = list_request, title = "Compre y venda criptomonedas en cuestión de minutos", isPurchase = True)

        if "buy" in request.form:
            list_request = {
                "coin_from": form.coin_from.data,
                "coin_to": form.coin_to.data,
                "quantity_from": form.quantity_from.data,
                "quantity_to": "",
                "value_unit": ""
            }

            if form.validate_on_submit():

                now = datetime.now()

                insert_movement([now.strftime("%Y-%m-%d"),
                        now.strftime("%H:%M:%S"),
                        form.coin_from.data,
                        float(form.quantity_from.data),
                        form.coin_to.data,
                        float(form.quantity_to.data)])

                flash("¡Su transacción ha sido realizada correctamente!")
                return redirect(url_for('history'))
            else:
                return render_template("purchase.html", msgError={}, form = form, list_request = list_request, title = "Compre y venda criptomonedas en cuestión de minutos", isPurchase = True)

@app.route("/status")
def status():

    status = get_status()
    current_value = current_total_value()

    return render_template("status.html", status = status, value = current_value, title = "Controle el estado de su inversión", isStatus = True, result = 0)

@app.route("/disclosures")
def disclosures():
    return render_template("disclosures.html", title = "Menciones legales para clientes de Tradue")