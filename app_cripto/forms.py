from flask_wtf import FlaskForm
from wtforms import StringField,DateField,FloatField,SubmitField
from wtforms.validators import DataRequired,Length,ValidationError

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])