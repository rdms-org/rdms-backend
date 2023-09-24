import pymysql
from dotenv import load_dotenv
import os
from bcrypt import checkpw

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

#로그인시 id와 pw 검사
def loginAuth(id,pw):
    sql = f"SELECT password FROM rdms_accounts WHERE username=%s"
    cursor.execute(sql,(id,))
    result = cursor.fetchall()
    if len(result)==1:
        #비밀번호 비교
        if checkpw(pw.encode('utf-8'),result[0][0].encode('utf-8')):
            return True
        else:
            return False
    else:
        return False
