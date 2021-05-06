FROM python:3-alpine
RUN apk add --update python3 py3-pip py3-flask; pip3 install --no-cache-dir flask flask-api
ADD ./app.py ./app.py 
#ENV PYTHONPATH /usr/lib/python3.9/site-packages 
CMD python3 app.py
EXPOSE 80


