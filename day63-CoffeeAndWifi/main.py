#Coffe and Wifi
#Ashlynn Ward, August 3, 2025
#This website shows a wifi rating for different cafes. Anyone can navigate to the homepage and info table. However, those who know about
#it can access an additional page that allows them to add cafes to the site. Their inputs are then added to the cafe csv.

#Import modules
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

#Create class for form
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time', validators=[DataRequired()])
    close_time = StringField('Closing Time', validators=[DataRequired()])
    coffee = SelectField('Coffe Rating', validators=[DataRequired()], choices = [(0, "✘"), (1, "☕️"), (2, "☕️☕️"), (3, "☕️☕️☕️"), (4, "☕️☕️☕️☕️"), (5, "☕️☕️☕️☕️☕️")])
    wifi = SelectField('Wifi Rating', validators=[DataRequired()], choices = [(0, "✘"), (1, "💪"), (2, "💪💪"), (3, "💪💪💪"), (4, "💪💪💪💪"), (5, "💪💪💪💪💪")])
    power = SelectField('Power Outlet Rating', validators=[DataRequired()], choices = [(0, "✘"), (1, "🔌"), (2, "🔌🔌"), (3, "🔌🔌🔌"), (4, "🔌🔌🔌🔌"), (5, "🔌🔌🔌🔌🔌")])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    #If form is submitted, add info to csv
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

#Run app
if __name__ == '__main__':
    app.run(debug=True)
