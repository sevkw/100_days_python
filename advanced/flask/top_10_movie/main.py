from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

#-------------------------------------Movie Search API---------------------------------------------#

load_dotenv(".env.movies")
# TMDB_TOKEN = os.getenv("TMDB_API_READ_TOKEN")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_URL = "https://api.themoviedb.org/3/search/movie"
# TMDB_URL_DETAIL = "https://api.themoviedb.org/3/movie/"
#-------------------------------------Flask App---------------------------------------------#

app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )

# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()

class MovieForm(FlaskForm):
    # no need to have DataRequired() validator b.c sometimes user may not want to update everything
    new_rating = DecimalField(places=1, label="Your Rating Out of 10 e.g.7.5")
    new_review = StringField(label="Your Review")
    submit = SubmitField(label="Done")

class FindMovie(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")

#-------------------------------------Flask---------------------------------------------#
@app.route("/")
def home():
    # get data from movies.db to display on the homepage
    with app.app_context():
        # all_movies = db.session.execute(db.select(Movie)).scalars().all()
        ## select movies and sort by rating with highest being the top ranked
        sorted_movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()
        for i in range(len(sorted_movies)):
            sorted_movies[i].ranking = i + 1
    return render_template("index.html", movies=sorted_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = MovieForm()
    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(Movie, movie_id)
    
    # if form has been validated upon submission
    if form.validate_on_submit():
        # update db data
        movie_selected.rating = form.new_rating.data
        movie_selected.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', movie_to_update=movie_selected, form=form)

@app.route("/delete")
def delete_movie():
    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_selected)
    db.session.commit()

    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovie()
    if form.validate_on_submit():
        search_title = form.title.data
        search_headers = {
            "query": search_title,
            "accept": "application/json",
            "api_key": TMDB_API_KEY
        }
        results = requests.get(TMDB_URL, params=search_headers).json()["results"]
        return render_template('select.html', movies=results)        

    return render_template('add.html', form=form)

@app.route("/find")
def find_movie():
    movie_id = request.args.get('api_id')
    if movie_id:
        details_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        details = requests.get(details_url, 
                               params={
                                   "accept": "application/json",
                                   "api_key": TMDB_API_KEY
                                   }
                            ).json()
        movie_title = details["title"]
        movie_overview = details["overview"]
        release_year = int(details["release_date"][:4])
        img_url = f"https://image.tmdb.org/t/p/w500{details['poster_path']}"
        # print(movie_title, release_year, img_url)
        # add the selected movie to the database
        new_movie = Movie(
            title=movie_title,
            year=release_year,
            description=movie_overview,
            img_url=img_url
            )
        db.session.add(new_movie)
        db.session.commit()
        # args.get will pick up the id defined below
        return redirect(url_for('edit', id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)

