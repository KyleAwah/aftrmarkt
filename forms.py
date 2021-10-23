#  Kyle Awah     - (816012635)
#
#  AFTR_MARKT
#  INFO 2602 - Web Programming and Technologies 1 
#
#  forms.py contains:
#  - FLASK WTF objects for the login


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email

class SignUp(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[Email(), InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('SIGN UP', render_kw={'id': 'Login_BTNN'})

class LogIn(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('LOGIN', render_kw={'id': 'Login_BTNN'})

class EditUser(FlaskForm):
    email = StringField('New Email:', validators=[Email()])
    password = PasswordField('New Password:')
    shipping_address = StringField('New Shipping Address:')
    payment_method = StringField('New Card Type')
    payment_method_card_number = StringField('Card Number:')
    submit = SubmitField('SAVE CHANGES', render_kw={'id': 'Login_BTNN'})
