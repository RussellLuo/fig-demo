# Dockerfile for building Flask-Web-App images
# Based on phusion/baseimage:latest

FROM phusion/baseimage:latest
MAINTAINER RussellLuo <luopeng.he@gmail.com>

# Update apt-get sources AND install pip
RUN apt-get update && apt-get install -y python-pip

# Install dependencies of the app
RUN mkdir -p /app
ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
