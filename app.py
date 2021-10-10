from flask import Flask, render_template, request
from gpiozero import OutputDevice


app = Flask(__name__)
relay = OutputDevice(14)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        relay.toggle()

    return render_template('index.html')

@app.route('/cake', methods=['POST'])
def cake():
    return render_template('cake.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')