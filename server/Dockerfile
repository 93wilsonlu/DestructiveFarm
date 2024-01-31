FROM python:3.11
MAINTAINER 93wilsonlu

WORKDIR /server
COPY . .
RUN apt-get update -y && apt-get install -y netcat iputils-ping
RUN pip install -r requirements.txt

RUN mkdir data && chown daemon data
USER daemon
ENTRYPOINT ["./start_server.sh"]