```
docker image build -t devk-hello-docker:1.0 .
docker run -d --name web1 -p 8085:80 devk-hello-docker:1.0
```
