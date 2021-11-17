from flask import Flask, render_template, request
from gpiozero import OutputDevice


app = Flask(__name__)
relay = OutputDevice(14)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        relay.toggle()

    return relay.is_lit()



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
