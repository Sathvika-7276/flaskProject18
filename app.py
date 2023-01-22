from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/<celsius>')
def celsius_to_fahrenheit(celsius=""):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f'The user input is {celsius} degrees which converted gives {fahrenheit:.2f} F'


if __name__ == '__main__':
    app.run()
