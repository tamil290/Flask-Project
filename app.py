from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1> Hello World! </h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello!"


def cel_to_fahren(cel):
    return cel * 9.0 / 5.0 + 32


@app.route('/convert/<celsius>')
def convert(cel):
    fahrenheit = cel_to_fahren(float(cel))
    return f"The temperature in Fahrenheit is {fahrenheit}"


app.run(debug=True)