import redis
import os
import json
from time import sleep
from random import randint

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')
    r = redis.Redis(host=redis_host, port=6379, db=0)
    print('Esperando mensaje...')
    while True:
        task = json.loads(r.blpop('sender')[1])
        print('Mandando mensaje:', task['subject'])
        sleep(randint(15, 45))
        r.lpush('tasks', json.dumps(task))
        print('mensaje enviado:', task['subject'], 'enviado')
        