```
docker image build -t ex-build-arg .
docker run ex-build-arg bash -c 'echo $S3_BUCKET'
```
```
docker image build --build-arg S3_BUCKET=mybucket -t ex-build-arg  .
docker run --rm ex-build-arg bash -c 'echo $S3_BUCKET'
docker image inspect --format="{{ index .Config.Labels.maintainer}}" ex-build-arg
```