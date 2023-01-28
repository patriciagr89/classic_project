from app_cripto import app
from flask import Flask, render_template, request
from app_cripto.models import *

@app.route("/")
def index():
    registros = select_all()
    return render_template("index.html", movements = registros, isIndex = True)

@app.route("/purchase", methods = ["POST","GET"])
def purchase():
    return render_template("purchase.html", isPurchase = True)

@app.route("/status")
def status():
    status = select_status()
    return render_template("status.html", movements = status, isStatus = True)

