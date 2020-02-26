FROM ubuntu:14.04
RUN apt-get update
RUN	apt-get install -y python3 python-pip 
#RUN	pip install random sys 
RUN	mkdir -p /home/dev/project/

WORKDIR /home/dev/project