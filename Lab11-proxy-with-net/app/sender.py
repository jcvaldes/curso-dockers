import psycopg2
import redis
import json
import os
from bottle import Bottle, route, run, request

# DSN = 'dbname=email_sender user=postgres password=postgres port=5439 host=0.0.0.0'
DSN = 'dbname=email_sender user=postgres password=postgres port=5432 host=db'
SQL = 'INSERT INTO emails (subject, message) VALUES (%s, %s)'

def register_message(subject, message):
    conn = psycopg2.connect(DSN)
    cur = conn.cursor()
    cur.execute(SQL, (subject, message))
    conn.commit()
    cur.close()
    conn.close()
    print('mensaje registrado !')


@route('/', method='POST')
def send():
    subject = request.forms.get('subject')
    message = request.forms.get('message')
    register_message(subject, message)
    return 'mensaje recibido ! asunto: {} message: {}'.format(
        subject, message
    )


if __name__ == '__main__':
    run(host='0.0.0.0', port=3000, debug=True)
