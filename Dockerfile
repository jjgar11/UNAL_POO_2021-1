FROM python:3.8-alpine3.13

WORKDIR /DOCKER_2021
COPY requirements.txt requirements.txt
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip3 install Pillow
COPY . .

CMD [ "python3", "/DOCKER_2021/back-end/proyecto.py" ]
