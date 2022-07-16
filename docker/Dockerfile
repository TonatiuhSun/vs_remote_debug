FROM docker.nextiva.xyz/nextiva-python:3.9-slim-buster

LABEL project=remote_debugging
LABEL service=app

COPY ./ /service
WORKDIR /service

ENV PYTHONPATH="/service"
ENV PYTHONUNBUFFERED=0

RUN pip install -U pip
# ---Install python dependencies---
RUN pip3 install -r ./requirements/app.txt

#CMD [ "python3", "uB -m debugpy --listen 0.0.0.0:5005 -m src.web.app" ]
#CMD [ "python", "-uB -m src.web.app" 