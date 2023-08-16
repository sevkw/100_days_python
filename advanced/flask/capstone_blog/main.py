from flask import Flask, render_template
import requests

blog_url = "https://api.npoint.io/9f0ec336aa9464fe79cb"
all_posts = requests.get(blog_url).json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/about')
def get_about():
    return render_template("about.html")

@app.route('/contact')
def get_contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
