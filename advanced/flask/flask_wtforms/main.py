from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from flask_wtf.csrf import CSRFProtect

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(max=30)])
    password = StringField('Password', validators=[DataRequired(), Length(max=30)])


app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = "123456"

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return "<h1>Login Successful!</h1>"
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)