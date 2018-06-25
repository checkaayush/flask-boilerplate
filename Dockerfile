FROM python:3.6-slim
LABEL maintainer="Aayush Sarva" email="checkaayush@gmail.com"

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app
EXPOSE 5000
CMD gunicorn -b 0.0.0.0:5000 --timeout 300 skaffold:app
