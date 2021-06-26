```
docker image build -t ex-build-copy:1.0 .
docker run -d --name web3 -p 8090:80 ex-build-copy:1.0
```