from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class BudgetForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    value = IntegerField('Сумма', validators=[NumberRange(min=1, message='Минимальное значение суммы = 1')])
    submit = SubmitField('Готово')



