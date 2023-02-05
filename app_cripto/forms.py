from flask_wtf import FlaskForm
from wtforms import StringField,DateField,FloatField,SubmitField,SelectField
from wtforms.validators import DataRequired,ValidationError
from datetime import date
from app_cripto.routes import *

class MyForm(FlaskForm):
    coin_from = SelectField('Moneda origen', choices=[], validators=[
        DataRequired(message="Debe seleccionar una moneda origen")])
    
    quantity_from = FloatField('Cantidad a invertir', validators=[
        DataRequired(message="Cantidad invalida: La cantidad a invertir es requerida, debe ser mayor a 0")])
    
    coin_to= SelectField('Moneda destino', choices=[], validators=[
        DataRequired(message="Debe seleccionar una moneda destino")])
    
    quantity_to = FloatField('Cantidad recibida')
    
    value_unit = FloatField('Valor unitario')
    
    calculate = SubmitField('')
    buy = SubmitField('Realizar transaccion')


    def validate_coin_from(form, field):
        if form.coin_from.data == form.coin_to.data:
            raise ValidationError("Moneda invalida: La moneda origen debe ser diferente a la moneda destino")
    
    def validate_coin_to(form, field):
        if form.coin_from.data == form.coin_to.data:
            raise ValidationError("Moneda invalida: La moneda origen debe ser diferente a la moneda destino")
    