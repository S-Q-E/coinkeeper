from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class NewPostForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    content = TextAreaField('Текст', validators=[DataRequired()])
    submit = SubmitField('Готово')
