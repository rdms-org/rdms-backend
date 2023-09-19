import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

#DB 연결용 변수
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

#DB 연결
print(DB_HOST)
db = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME, charset='utf8')
cursor = db.cursor()
print("test")

#로그인시 id와 pw로 존재여부 검사
def loginAuth(id,pw):
    sql = f"SELECT id FROM rdms_accounts WHERE identity='{id}' AND password='{pw}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    return len(result)==1