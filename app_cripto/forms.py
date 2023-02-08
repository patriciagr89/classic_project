from flask_wtf import FlaskForm
from wtforms import FloatField,SubmitField,SelectField, StringField, DecimalField
from wtforms.validators import DataRequired,ValidationError
from app_cripto.routes import *
from app_cripto.custom_validators import *

class MyForm(FlaskForm):
    coin_from = SelectField('Moneda origen', choices=[], validators=[
        DataRequired(message="Error: Debe seleccionar una moneda origen"), NotEqualTo("coin_to", message="Error: Moneda origen seleccionada debe ser diferente a moneda destino")])
    
    quantity_from = FloatField('Cantidad a invertir', validators=[
        DataRequired(message="Error: Cantidad a invertir es requerida, debe ser un número mayor a 0")])
    
    coin_to= SelectField('Moneda destino', choices=[], validators=[
        DataRequired(message="Error: Debe seleccionar una moneda destino, debe ser diferente a moneda origen"), NotEqualTo("coin_from", message="Error: Moneda origen seleccionada debe ser diferente a moneda destino")])
    
    quantity_to = StringField('Cantidad recibida')
    
    value_unit = StringField('Valor unitario')
    
    calculate = SubmitField('')
    buy = SubmitField('Realizar transacción')


    # def validate_coin_to(form, field):
    #     if form.coin_from.data == form.coin_to.data:
    #         raise ValidationError("Moneda invalida: La moneda origen debe ser diferente a la moneda destino")

    def validate_quantity_from(form, field):
        if "EUR" != form.coin_from.data:
            balances = get_balance()
            for item in balances:
                if item["cripto"] == form.coin_from.data and float(item["balance"]) < float(form.quantity_from.data):
                    raise ValidationError("Error: No dispone de saldo suficiente")

    def validate_value_unit(form, field):
        if form.value_unit.data is None or form.value_unit.data == "":
            raise ValidationError("Error: Pulse el botón calcular para continuar")
        if float(form.quantity_to.data) != float(form.quantity_from.data) * float(form.value_unit.data):
            raise ValidationError("Error: Pulse el botón calcular para continuar")

    def validate_quantity_to(form, field):
        if form.quantity_to.data is None or form.quantity_to.data == "":
            raise ValidationError("Error: Pulse el botón calcular para continuar")
        if float(form.quantity_to.data) != float(form.quantity_from.data) * float(form.value_unit.data):
            raise ValidationError("Error: Pulse el botón calcular para continuar")
