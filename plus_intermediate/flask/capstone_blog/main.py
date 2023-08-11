from flask import Flask, render_template
import requests


app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
all_posts = requests.get(blog_url).json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:blog_id>')
def get_blog(blog_id):
    
    return render_template("post.html", posts=all_posts, post_id=blog_id)

if __name__ == "__main__":
    app.run(debug=True)
