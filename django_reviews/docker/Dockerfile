# image
FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN apk add --no-cache mariadb-connector-c-dev ;\
    apk add --no-cache --virtual .build-deps \
        build-base \
        mariadb-dev ;\
    pip install mysqlclient;\
    apk add gcc python3-dev jpeg-dev zlib-dev ;\
    pip install Pillow
    
RUN pip install -r requirements.txt

RUN apk del .build-deps

RUN mkdir /app

WORKDIR /app
COPY . /app


RUN adduser -D user
USER user

# ENTRYPOINT ["/app/entrypoint.sh"]