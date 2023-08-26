# import sqlite3

# db = sqlite3.connect("books-collection.db")

# cursor = db.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS books\
#                (id INTEGER PRIMARY KEY\
#                 , title varchar(250) NOT NULL UNIQUE\
#                 , author varchar(250) NOT NULL\
#                 , rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books\
#                VALUES(1, 'Harry Potter', 'J.K.Rowling', '9.3')")

# db.commit()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Books {self.title}>'

with app.app_context():
    db.create_all()

# Insert Data into the new table
with app.app_context():
    new_book = Books(id=1, title='Harry Potter', author='J.K.Rowling', rating=9.3)
    db.session.add(new_book)
    db.session.commit()