# Secrets
#Ashlynn Ward, July 11, 2025
#The purpose of this website is to learn howt o use WTForms for login. Once a user has successfully logged in, the website will show
#some secrets to them.

#Import modules
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5 

#Define form class
class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='submit')

app = Flask(__name__)
bootstrap = Bootstrap5(app)

#Open home page
@app.route("/")
def home():
    return render_template('index.html')

#Open login page
@app.route("/login", method=["GET", "POST"])
def login():
    login_form = MyForm()
    #Validate form submission
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)

#Run app
if __name__ == '__main__':
    app.run(debug=True)
