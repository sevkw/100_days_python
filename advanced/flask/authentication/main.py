from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CREATE TABLE IN DB with the UserMixin
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/secrets')
# only authenticated users can access the secrets page
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # or request.form.get("email") would also work
        input_email = request.form["email"]
        input_name = request.form["name"]
        # hash the password
        hashed_password = generate_password_hash(request.form["password"], method="pbkdf2:sha256", salt_length=8)
        new_user = User(
            email=input_email,
            name=input_name,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()

        #log user in upon registration
        login_user(new_user)

        return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        # match user via email
        user_to_login = db.session.execute(db.select(User).where(User.email == email)).scalar()

        # check if hashed password entry matches the hash in db
        if check_password_hash(user_to_login.password, password):
            login_user(user_to_login)
            return redirect(url_for('secrets'))

    return render_template("login.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory(
        'static',path="files/cheat_sheet.pdf", as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
