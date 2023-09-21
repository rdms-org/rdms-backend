FROM python:3.11

COPY . /usr/src/app

RUN pip install flask
RUN pip install Flask-Cors
RUN pip install python-dotenv
RUN pip install pymysql
RUN pip install bcrypt

WORKDIR /usr/src/app

CMD ["python", "./app.py"]