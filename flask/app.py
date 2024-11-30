from flask import Flask

app = Flask(__name__)


@app.route('/info', methods=['GET'])

def info():
    health = 'Application is running!'

    return {'health': health }, 200
