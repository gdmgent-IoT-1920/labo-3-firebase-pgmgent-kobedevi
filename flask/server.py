from flask import Flask, render_template, request
from sense_hat import SenseHat
from PIL import ImageColor

# sensehat instantiëren
sense = SenseHat()

# flask server instantiëren
app = Flask(__name__)

sense_values = {
    'value': '#000000',
    'type': 'hex'
}

@app.route('/')
def index():
    return 'Hello World'

@app.route('/hello')
def hello():
    return 'say hi!'

@app.route('/sensehat', methods=['GET', 'POST'])
def sensehat():
    if(request.method == 'POST'):
        sense_values['value'] = request.form['senseColor']

        sense.clear(ImageColor.getrgb(sense_values['value']))

    return render_template('sensehat.html.j2', sense_values = sense_values)

# server constants
host = '192.168.0.142'
port = 8080
if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)