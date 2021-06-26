```
docker image build -t ex-build-dev .

docker container run -it -v $(pwd):/app -p 8077:8000 --name python-server ex-build-dev
```

## Accedo a traves de un volumen creado en el container python-server a traves de otro contenedor
```
docker container run -it --volumes-from=python-server debian cat /log/http-server.log
```