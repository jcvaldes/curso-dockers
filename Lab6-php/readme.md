docker-compose up -d --force-recreate


# Tarea

Armar un servicio de docker conservidor nginx para publicar el frontend

ejem: docker-compose.yml

```
web-prod:
  image: nginx
  container_name: "cdxar-web-prod"
  restart: always
  ports:
      - 8081:80
  links:
    - nodeapp-prod
  volumes:
    - ./config/nginx/nginx.conf:/etc/nginx/nginx.conf
    # - ./config/nginx/default.conf:/etc/nginx/conf.d/default.conf
    - ./config/nginx/web.conf:/etc/nginx/conf.d/default.conf
    - ./client/dist/credexar:/usr/share/nginx/html:ro
```