import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/healthz', methods=['GET'])
def about():
    healthz = 'Application is running!'

    return {'healthz': healthz}, 200


@app.route('/environment', methods=['GET'])
def secrets():
    creds = dict()

    creds['env-1'] = os.environ.get('ENV_VALUE')
    creds['env-2'] = os.environ.get('ENV_TOKEN')

    return creds, 200


@app.route('/records', methods=['GET', 'POST'])
def volumes():
    filename = '/data/test'

    if request.method == 'POST':
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            f.write('Customer record')

        return 'Saved!', 201
    else:
        f = open(filename, 'r')

        return f.read(), 200
