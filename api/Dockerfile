FROM python:3.11

COPY . /usr/src/app

RUN pip install flask
RUN pip install Flask-Cors
RUN pip install pymysql

WORKDIR /usr/src/app

CMD ["python", "./app.py"]