from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # loop through each column in data record
        return {column.name:getattr(self, column.name) for column in self.__table__.columns}



with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record

## A /random route that allows GET request
@app.route("/random")
def get_random_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = choice(all_cafes)
    # return jsonify(cafe={"id": random_cafe.id,
    #                      "name": random_cafe.name,
    #                      "map_url": random_cafe.map_url,
    #                      "img_url": random_cafe.img_url,
    #                      "location": random_cafe.location,
    #                      "has_sockets" : random_cafe.has_sockets,
    #                      "has_toilet": random_cafe.has_toilet,
    #                      "has_wifi": random_cafe.has_wifi,
    #                      "can_take_calls" : random_cafe.can_take_calls,
    #                      "seats": random_cafe.seats,
    #                      "coffee_price" : random_cafe.coffee_price
    # }
    # )
    return jsonify(cafe=random_cafe.to_dict())
## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
