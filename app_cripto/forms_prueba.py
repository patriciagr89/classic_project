# from flask_wtf import FlaskForm
# from wtforms import FloatField,SubmitField,SelectField, StringField, DecimalField
# from wtforms.validators import DataRequired,ValidationError
# from app_cripto.routes import *
# from app_cripto.custom_validators import *

# class MyForm(FlaskForm):
#     coin_from = SelectField('Moneda origen', choices=[], validators=[
#         DataRequired(message="Error: Debe seleccionar una moneda origen"), NotEqualTo("coin_to", message="Error: Moneda origen debe ser diferente a moneda destino")])
    
#     quantity_from = FloatField('Cantidad a invertir', validators=[
#         DataRequired(message="Error: Cantidad a invertir es requerida")])
    
#     coin_to= SelectField('Moneda destino', choices=[], validators=[
#         DataRequired(message="Error: Debe seleccionar una moneda destino, debe ser diferente a moneda origen"), NotEqualTo("coin_from", message="Error: Moneda origen debe ser diferente a moneda destino")])
    
#     quantity_to = StringField('Cantidad recibida')
    
#     value_unit = StringField('Valor unitario')
    
#     calculate = SubmitField('')
#     buy = SubmitField('Realizar transacción')


#     def validateForm(requestForm):
#         errores=[]
#         if "EUR" != requestForm["coin_from"]:
#             balances = get_balance()
#             for item in balances:
#                 if item["cripto"] == requestForm["coin_from"] and float(item["balance"]) < float(requestForm["quantity_from"]):
#                     errores.append("Error: No dispone de saldo suficiente")

#         if requestForm["value_unit"] is None or requestForm["value_unit"] == "":
#             errores.append("Error: Sin datos")
#         if float(requestForm["quantity_to"]) != float(requestForm["quantity_from"]) * float(requestForm["value_unit"]):
#             errores.append("Error: Recalcule para continuar. Modificación detectada ")
        
#         if requestForm["quantity_to"] is None or requestForm["quantity_to"] == "":
#            errores.append("Error: Sin datos")
#         if float(requestForm["quantity_to"]) != float(requestForm["quantity_from"]) * float(requestForm["value_unit"]):
#             errores.append("Error: Recalcule para continuar. Modificación detectada")

        