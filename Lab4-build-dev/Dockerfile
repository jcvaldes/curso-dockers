FROM python:3.6
LABEL maintainer="Juan Carlos Valdés <idevkingos@gmail.com>"

RUN useradd www && \
    mkdir /app && \
    mkdir /log && \
    chown www /log

# usuario que va a estar logueado
USER www

# configuro como volumen en el contenedor para compartir 
# con otro contenedor que luego voy a crear
VOLUME /log

# directorio de trabajo
WORKDIR /app

# expongo la puerta del codigo de python
EXPOSE 8000

ENTRYPOINT [ "/usr/local/bin/python" ]
# paso el comando al entrypoint
CMD ["run.py"]