FROM python:3.6.8-jessie as latest

MAINTAINER timurmardanov97@gmail.com

# project directory
RUN mkdir project
WORKDIR project

# copy all elements
COPY . /project

RUN apt-get -y update && apt-get -y upgrade

COPY requirements.txt /project
RUN pip3 install -U -q -r requirements.txt

EXPOSE 80

CMD ["python3", "chatapp/main.py"]
