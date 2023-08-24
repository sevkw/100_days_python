from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
csv_path = 'cafe-data.csv'


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = URLField('Cafe Location on Google Maps (URL)', validators=[DataRequired()])
    open_time = StringField('Opening Time e.g.8AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g.5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField(u'Coffee Rating', choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'])
    wifi_rating = SelectField(u'Wifi Strength Rating', choices=['✘','💪','💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    power_rating = SelectField(u'Power Socket Availability', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField(label='Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = [form.cafe.data,
                    form.location_url.data,
                    form.open_time.data,
                    form.close_time.data,
                    form.coffee_rating.data,
                    form.wifi_rating.data,
                    form.power_rating.data]
        with open(csv_path, mode="a", encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(new_cafe)
        with open(csv_path, newline='', encoding='utf-8') as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            list_of_rows = []
            for row in csv_data:
                list_of_rows.append(row)
        return render_template('cafes.html', cafes=list_of_rows)

        # print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(csv_path, newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
