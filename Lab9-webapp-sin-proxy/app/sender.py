import psycopg2
import redis
import json
import os
from bottle import Bottle, request


class Sender(Bottle):
    def send(self):
        subject = request.forms.get('subject')
        message = request.forms.get('message')

        return 'Mensaje recibido ! Asunto: {} Mensaje: {}'.format(
            subject, message
        )

if __name__ == '__main__':
    sender = Sender()
    sender.run(host='0.0.0.0', port=3000, debug=True)