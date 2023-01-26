from app_cripto import app
from flask import render_template
from app_cripto.models import *

@app.route("/")
def index():
    registros = select_all()
    return render_template("index.html", data = registros)

@app.route("/purchase")
def purchase():
    return render_template("purchase.html")

@app.route("/status")
def status():
    status = select_status()
    return render_template("status.html", data = status)

