from flask import Flask
import random

app = Flask(__name__)

answer = random.randint(0, 9)
# print(f"check: answer is {answer}")

@app.route("/")
def home():
    return "<h1 style='text-align: center'> Guess a number between 0 and 9 :) </h1> "\
           "<center><img src='https://media.giphy.com/media/zJWAkCpWNrd6w/giphy-downsized-large.gif'></center>"

@app.route("/<int:guess>")
def validate_guess(guess):
    if guess < answer:
        return "<h1 style='text-align: center'>Too low, try again! </h1> "\
               "<center><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></center>"
    elif guess > answer:
        return "<h1 style='text-align: center'>Too large, try again! </h1> "\
               "<center><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></center>"
    elif guess == answer:
        return "<h1 style='text-align: center'>You found me!</h1> "\
               "<center><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></center>"

if __name__ == "__main__":
    app.run(debug=True)