import os
from flask import Flask

app = Flask(__name__)


@app.route('/info', methods=['GET'])

def info():
    health = 'Application is running!'

    return {'health': health }, 200

@app.route('/env', methods=['GET'])

def env():
    value = os.environ.get('ENV_VALUE')

    return {'value': value}, 200

@app.route('/creds', methods=['GET'])

def creds():
    values = dict()

    # values['secure'] = open("/run/secrets/token", "r").read()
    values['insecure'] = os.environ.get('ENV_TOKEN')

    return values, 200
