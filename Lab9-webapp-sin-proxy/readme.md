```
docker pull postgres
mkdir -p $HOME/docker/volumes/postgres
docker run --name postgres1 -p 5437:5432 -v ~/docker/volumes/postgres:/var/lib/postgresql/data -e POSTGRES_PASSWORD=postgres -d postgres
docker exec -ti postgres1 psql -U postgres
alter user postgres with password 'postgres';
CREATE DATABASE credexar;
# psql -h localhost -U postgres -d postgres
```

```
docker-compose up -d

docker-compose exec db psql -U postgres -d postgres -c '\l'
docker-compose exec db psql -h localhost -U postgres -d postgres
docker-compose exec db psql -U postgres -d postgres -f /scripts/check.sql

docker-compose -f docker-compose-uat.yml start

dpcker-compose logs -f -t

```

si se quiere recrear la base de datos por primera vez borro el volumen fisicamente
