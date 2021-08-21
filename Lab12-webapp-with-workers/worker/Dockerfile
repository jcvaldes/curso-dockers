FROM python:3.7

RUN useradd --create-home appuser

RUN apt-get update --fix-missing && \
  apt-get install postgresql -y && \
  apt-get install libpq5 -y && \
  apt-get install libpq-dev -y && \
  apt-get install apt-utils -y

ENV PYTHONUNBUFFERED 1

USER appuser
RUN pip install redis 
ENTRYPOINT ["python"]

# EXPOSE 3000


# WORKDIR /home/appuser

# CMD ["/bin/bash"]
# CMD [ "python", "sender.py" ]