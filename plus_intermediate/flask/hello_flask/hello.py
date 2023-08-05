from flask import Flask

app = Flask(__name__)

def make_bold(function):
    """A decorator that makes content bold by adding <b></b> tag."""
    def wrapper():
        content = function()
        return f"<b> {content} </b>"
    return wrapper

def emphasis(function):
    """A decorator adds emphasis to content through adding <em> tag."""
    def wrapper():
        content = function()
        return f"<em> {content} </em>"
    return wrapper

def underline(function):
    """A decorator that add underline tag to HTML content."""
    def wrapper():
        content = function()
        return f"<u> {content} </u>"
    return wrapper

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'> Hello, World! </h1>" \
           "<p> This is a paragraph </p>" \
           "<img src='https://media.giphy.com/media/aCqb9YW7QclN3rtto5/giphy-downsized-large.gif'width=400>"


@app.route("/bye")
@make_bold
@emphasis
@underline
def bye():
    return "Bye!"

# creating a variable paths and converting the path to a specified data type
@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)