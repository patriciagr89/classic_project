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

    def test(form):
        print("--------------------------------------")
        # print(form.quantity_from.data)
        print("--------------------------------------")
        # form.quantity_from.data = 44

    # def validate_coin_from(form):
    #     if form.coin_from.data != form.coin_to.data:
    #         raise ValidationError("Error: Moneda origen seleccionada debe ser diferente a moneda destino")
    
    # def validate_coin_to(form):
    #     if form.coin_from.data != form.coin_to.data:
    #         raise ValidationError("Error: Moneda origen seleccionada debe ser diferente a moneda destino")
    