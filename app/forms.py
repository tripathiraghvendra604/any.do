from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email

class AnyDoForm(Form):
    body = StringField(validators= [DataRequired()])