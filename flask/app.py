import os
import logging
from flask import Flask, request, jsonify
from psycopg_pool import ConnectionPool

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def dbConnect():
#     try:
#         db_host = os.environ.get('DB_HOST')
#         db_database = os.environ.get('DB_DATABASE')
#         db_user = os.environ.get('DB_USER')
#
#         db_password = open('/run/secrets/pg-password', 'r').read()
#
#         url = f'host={db_host} dbname={db_database} user={db_user} password={db_password}'
#
#         pool = ConnectionPool(url)
#         pool.wait()
#
#         with pool.connection() as conn:
#             logging.info('Successfully connected to the database.')
#
#             with conn.cursor() as cur:
#                 cur.execute("""
#                     CREATE TABLE IF NOT EXISTS records (
#                         id SERIAL PRIMARY KEY,
#                         content TEXT NOT NULL
#                     )
#                 """)
#                 conn.commit()
#
#         return pool
#
#     except Exception as e:
#         logging.error(f'Failed to connect to the database: {e}')
#         raise
#
# pool = dbConnect()

app = Flask(__name__)


@app.route('/healthz', methods=['GET'])
def about():
    healthz = 'Application is running!'
    return {'healthz': healthz}, 200

@app.route('/volumes', methods=['GET', 'POST'])
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

@app.route('/environment', methods=['GET'])
def secrets():
    creds = dict()
    creds['env-1'] = os.environ.get('ENV_VALUE')
    creds['env-2'] = os.environ.get('ENV_TOKEN')
    return creds, 200


# @app.route('/records', methods=['POST', 'GET'])
# def records():
#     if request.method == 'POST':
#         try:
#             content = request.json.get('content', '')
#             if not content:
#                 return {'error': 'Content is required'}, 400
#
#             with pool.connection() as conn:
#                 with conn.cursor() as cur:
#                     cur.execute("INSERT INTO records (content) VALUES (%s) RETURNING id", (content,))
#                     record_id = cur.fetchone()[0]
#                     conn.commit()
#
#             return {'message': 'Record inserted successfully', 'id': record_id}, 201
#
#         except Exception as e:
#             logging.error(f'Error inserting record: {e}')
#             return {'error': str(e)}, 500
#
#     elif request.method == 'GET':
#         try:
#             with pool.connection() as conn:
#                 with conn.cursor() as cur:
#                     cur.execute("SELECT id, content FROM records")
#                     rows = cur.fetchall()
#
#             records = [{'id': row[0], 'content': row[1]} for row in rows]
#             return jsonify(records), 200
#
#         except Exception as e:
#             logging.error(f'Error fetching records: {e}')
#             return {'error': str(e)}, 500

