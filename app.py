# Flask interface placeholder

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'NeuroScent Flask Interface'

if __name__ == '__main__':
    app.run(debug=True)
