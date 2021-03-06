FROM python:3-alpine
RUN apk add --update python3 py3-pip py3-flask; pip3 install --no-cache-dir flask flask-api gunicorn flake8 pytest requests
WORKDIR /APP
ADD ./app.py ./app.py 
ADD ./input.html ./input.html
ADD ./requirements.txt .
RUN pip3 install -r requirements.txt
ENV PYTHONPATH /usr/lib/python3.9/site-packages 
CMD python3 app.py
EXPOSE 5000
EXPOSE 80


