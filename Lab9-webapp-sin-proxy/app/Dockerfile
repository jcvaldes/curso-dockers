FROM python:3.9.5

#RUN useradd --create-home appuser

RUN apt-get update --fix-missing && \
  apt-get install postgresql -y && \
  apt-get install libpq5 -y && \
  apt-get install libpq-dev -y



#WORKDIR /home/appuser

#CMD [ "python", "./sender.py" ]