```
docker pull postgres
mkdir -p $HOME/docker/volumes/postgres
docker run --name postgres1 -p 5437:5432 -v ~/docker/volumes/postgres:/var/lib/postgresql/data -e POSTGRES_PASSWORD=postgres -d postgres
docker exec -ti postgres1 psql -U postgres
alter user postgres with password 'postgres';

CREATE DATABASE email_sender;
# psql -h localhost -U postgres -d postgres
```

```
docker-compose up -d

docker-compose exec db psql -U postgres -d postgres -c '\l'
docker-compose exec db psql -h localhost -U postgres -d postgres
docker-compose exec db psql -U postgres -d postgres -f /scripts/check.sql

docker-compose -f docker-compose-uat.yml start

dpcker-compose logs -f -t

// escalo instancias de un servicio determinado de docker en este caso el servicio se llama worker
docker-compose up -d --scale worker=3 --force-recreate


```

si se quiere recrear la base de datos por primera vez borro el volumen fisicamente


# consulto la db

docker-compose exec db psql -U postgres -d email_sender -c 'select * from emails'
