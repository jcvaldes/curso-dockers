FROM python:3.7

RUN useradd --create-home appuser

RUN apt-get update --fix-missing && \
  apt-get install postgresql -y && \
  apt-get install libpq5 -y && \
  apt-get install libpq-dev -y && \
  apt-get install apt-utils -y

USER appuser
RUN pip install bottle  && \
    pip install redis  && \
    pip install psycopg2 

# EXPOSE 3000


# WORKDIR /home/appuser

# CMD ["/bin/bash"]
# CMD [ "python", "sender.py" ]