import psycopg2
import redis
import json
import os
from bottle import route, run, request


@route('/', method='POST')
def send():
    subject = request.forms.get('subject')
    message = request.forms.get('message')

    return 'mensaje recibido ! asunto: {} message: {}'.format(
        subject, message
    )

if __name__ == '__main__':
    run(host='0.0.0.0', port=3000, debug=True)
