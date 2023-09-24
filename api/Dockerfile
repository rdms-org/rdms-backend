FROM python:3.11

COPY . /usr/src/app

ENV DB_HOST db
ENV DB_NAME rdms

#SQL 계정과 비밀번호는 추후 파일로 분리하여 관리할 예정
ENV DB_USER root
ENV DB_PASSWORD mysql_root_password

RUN pip install flask
RUN pip install Flask-Cors
RUN pip install python-dotenv
RUN pip install pymysql
RUN pip install bcrypt

WORKDIR /usr/src/app

CMD ["python", "./app.py"]