from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField, SubmitField,
                            SelectField, DateField, IntegerField, RadioField)
from wtforms.validators import DataRequired, length, equal_to
from flask_wtf.file import FileField


class RegisterForm(FlaskForm):
    username = StringField("შეიყვანე სახელი", validators=[DataRequired()])
    password = PasswordField("შეიყვანე პაროლი", validators=[DataRequired(),
                                                            length(min=8, max=32, message="პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო")])
    confirm_password = PasswordField("გაიმეორე პაროლი", validators=[DataRequired(),
                                                                    equal_to("password", message="პაროლები არ ემთხვევა")])


    submit = SubmitField("დარეგისტრირდი")


class LoginForm(FlaskForm):
    username = StringField("შეიყვანე სახელი")
    password = PasswordField("შეიყვანე პაროლი")

    submit = SubmitField("შესვლა")

class MovieForm(FlaskForm):
    image = FileField("Add movie Image")
    name = StringField("Add movie name")
    release_year = IntegerField("Add release year")

    submit = SubmitField("Add a movie")