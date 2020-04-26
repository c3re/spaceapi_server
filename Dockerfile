#Install the container's OS.
FROM ubuntu:latest 


# Install SPaceAPI-Server v0.3
RUN apt-get update
# Muss bei Update geändert werden.
RUN wget https://gitlab.com/s3lph/spaceapi-server/-/jobs/372554856/artifacts/raw/package/debian/spaceapi-server_0.3-1_all.deb
RUN apt-get install -y spaceapi-server_0.3-1_all.deb

#Install MQTTClient
RUN apt-get install -y mosquitto-clients

#CLEAR APT
RUN rm -rf /var/lib/apt/lists/*

#Delete Preconfig
RUN rm -rf /etc/spaceapi-server/*

#Compy c3RE Config
COPY /spaceapi-server/ /etc/spaceapi-server/


VOLUME /etc/spaceapi-server
EXPOSE 8080