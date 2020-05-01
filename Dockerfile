#Install the container's OS.
FROM ubuntu:latest 


# Install SPaceAPI-Server v0.3
RUN apt-get update
RUN apt-get install -y wget mosquitto-clients

# Muss bei Update geändert werden.
RUN wget https://gitlab.com/s3lph/spaceapi-server/-/jobs/372554856/artifacts/raw/package/debian/spaceapi-server_0.3-1_all.deb
RUN apt install -y ./spaceapi-server_0.3-1_all.deb

#Delete Preconfig
RUN rm -rf /etc/spaceapi-server/*

#Compy c3RE Config
COPY /spaceapi-server/ /etc/spaceapi-server/

ENTRYPOINT python3 -m spaceapi_server /etc/spaceapi-server/config.json
EXPOSE 8080
