FROM mysql:8.0

#SQL 계정과 비밀번호는 추후 파일로 분리하여 관리할 예정
ENV MYSQL_USER mysql_user
ENV MYSQL_PASSWORD mysql_password
ENV MYSQL_ROOT_PASSWORD mysql_root_password
ENV MYSQL_DATABASE rdms

#도커 환경에서 컨테이너 생성시 아래 스크립트 실행
COPY ./scripts/ /docker-entrypoint-initdb.d/

