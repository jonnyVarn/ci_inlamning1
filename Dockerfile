FROM alpine:latest
ADD ./app.py ./app.py
CMD apk update && apk add python3 py3-pip py-flask py-flask-api && python app.py
EXPOSE 5000


