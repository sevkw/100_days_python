from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def receive_data():
    input_name = request.form["username"]
    input_password = request.form["password"]
    return render_template("login.html", username=input_name, password=input_password)

if __name__ == "__main__":
    app.run(debug=True)