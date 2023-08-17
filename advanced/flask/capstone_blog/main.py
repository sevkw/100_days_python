from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv(".env.email")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_EMAIL_APP_PSWD = os.getenv("SENDER_EMAIL_APP_PSWD")
TO_EMAIL = os.getenv("TO_EMAIL")

blog_url = "https://api.npoint.io/9f0ec336aa9464fe79cb"
all_posts = requests.get(blog_url).json()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/about')
def get_about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def get_contact():
    if request.method == "POST":
        data = request.form
        message = data["message"]
        email = data["email"]
        username = data["username"]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_EMAIL_APP_PSWD)
            connection.sendmail(
                from_addr=SENDER_EMAIL, 
                to_addrs=TO_EMAIL,
                msg=f"Subject: Email from {username}!\n\nName: {username}\nEmail: {email}\nMessage: {message}"
            )
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)

@app.route('/post/<int:blog_id>')
def get_blog(blog_id):
    return render_template("post.html", posts=all_posts, post_id=blog_id)

if __name__ == "__main__":
    app.run(debug=True)
