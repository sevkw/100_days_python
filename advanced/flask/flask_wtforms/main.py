from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_wtf.csrf import CSRFProtect

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Please ensure Email Address entered is valid!", check_deliverability=True)])
    # password = StringField('Password', validators=[DataRequired(), Length(max=30)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Field must be at least 8 characters long.")])
    submit = SubmitField(label = 'Log In')


app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = "123456"

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return "<h1>Login Successful!</h1>"
        else:
            return "<h1>Access Denied</h1>"
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)