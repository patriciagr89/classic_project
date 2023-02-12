from flask_wtf import FlaskForm
from wtforms import SubmitField,SelectField, DecimalField, StringField
from wtforms.validators import DataRequired,ValidationError,EqualTo
from app_cripto.routes import *
from app_cripto.custom_validators import *


class MyForm(FlaskForm):
    coin_from = SelectField('Moneda origen', choices=[], validators=[
        DataRequired(message="Error: Debe seleccionar una moneda origen"), EqualTo("coin_from_validator", message="Error: Recalcule para continuar. Modificación de datos detectada"), NotEqualTo("coin_to", message="Error: Moneda origen debe ser diferente a moneda destino")])

    coin_from_validator = StringField('')

    quantity_from = DecimalField('Cantidad a invertir', validators=[
        DataRequired(message="Error: Cantidad a invertir es requerida")])

    coin_to= SelectField('Moneda destino', choices=[], validators=[
        DataRequired(message="Error: Debe seleccionar una moneda destino, debe ser diferente a moneda origen"), EqualTo("coin_to_validator", message="Recalcule para continuar. Modificación de datos detectada"), NotEqualTo("coin_from", message="Error: Moneda origen debe ser diferente a moneda destino")])
    
    coin_to_validator = StringField('')

    quantity_to = DecimalField('Cantidad recibida')
    
    value_unit = DecimalField('Valor unitario')
    
    calculate = SubmitField('')
    buy = SubmitField('Realizar transacción')


    def validate_quantity_from(form, field): #controla que el importe a invertir no se negativo y haya saldo suficiente
        if float(form.quantity_from.data) < 0.0:
            raise ValidationError("Error: No se pueden usar números negativos")
        if "EUR" != form.coin_from.data:
            balances = get_balance()
            for item in balances:
                if item["cripto"] == form.coin_from.data and float(item["balance"]) < float(form.quantity_from.data):
                    raise ValidationError("Error: No dispone de saldo suficiente")

    def validate_value_unit(form, field): #controla que haya datos en el campo antes de volcar en BBDD y no se hayan modificado ciertos campos despues de pulsar el boton de calcular
        if form.value_unit.data is None or form.value_unit.data == "":
            raise ValidationError("Error: Sin datos")
        if float(form.quantity_to.data) != float(form.quantity_from.data) * float(form.value_unit.data):
            raise ValidationError("Error: Recalcule para continuar. Modificación de datos detectada")

    def validate_quantity_to(form, field): #controla que haya datos en el campo antes de volcar en BBDD y no se hayan modificado ciertos campos despues de pulsar el boton de calcular
        if form.quantity_to.data is None or form.quantity_to.data == "":
            raise ValidationError("Error: Sin datos")
        if float(form.quantity_to.data) != float(form.quantity_from.data) * float(form.value_unit.data):
            raise ValidationError("Error: Recalcule para continuar. Modificación de datos detectada")