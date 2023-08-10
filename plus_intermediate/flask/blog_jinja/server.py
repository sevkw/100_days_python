from flask import Flask, render_template
import random
from datetime import datetime
import requests

GENDERIZE_ENDPOINT = "https://api.genderize.io"
AGIFY_ENDPOINT = "https://api.agify.io"

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/guess/<string:name>")
def guess(name):
    gender_api_param = {"name": {name}}
    agify_api_param = gender_api_param

    gender_response = requests.get(GENDERIZE_ENDPOINT, params=gender_api_param)
    client_gender = gender_response.json()["gender"]

    age_response = requests.get(AGIFY_ENDPOINT, params=agify_api_param)
    client_age = age_response.json()["age"]

    return render_template("guess.html", guess_name=name, guess_gender=client_gender, guess_age=client_age)

@app.route("/blog/<int:num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(blog_url).json()
    return render_template("blog.html", posts=all_posts, blog_num=num)


if __name__ == "__main__":
    app.run(debug=True)