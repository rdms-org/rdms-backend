import pymysql
from dotenv import load_dotenv
import os
from bcrypt import checkpw
from uuid import uuid1

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
def loginAuth(username, password):
    sql = f"SELECT password FROM rdms_accounts WHERE username=%s"
    cursor.execute(sql,(username,))
    result = cursor.fetchall()
    if len(result)==1:
        #비밀번호 비교
        if checkpw(password.encode('utf-8'),result[0][0].encode('utf-8')):
            return True
        else:
            return False
    else:
        return False

#루트어드민 여부 확인
def isRoot(username):
    sql = f"SELECT id FROM rdms_accounts WHERE username=%s AND root_permission=TRUE"
    cursor.execute(sql,(username,))
    result = cursor.fetchall()
    if len(result)==1:
        return True
    else:
        return False


#username으로 유저 정보 가져오기
def getUser(username):
    sql = f"SELECT id,name,username,root_permission,preference FROM rdms_accounts WHERE username=%s"
    cursor.execute(sql,(username,))
    result = cursor.fetchall()
    if len(result)==1:
        result = result[0]
        adminData = {
            "id":result[0],
            "name":result[1],
            "username":result[2],
            "root_permission":result[3],
            "perference":result[4]
            }
        return adminData
    else:
        return None

#중복되지 않는 UUID 생성
def GenerateUUID():
    while(True):
        uuid = uuid1()
        sql = f"SELECT uuid FROM rdms_devices WHERE uuid=%s;"
        cursor.execute(sql,(uuid,))
        result = cursor.fetchall()
        if len(result)==0:
            return uuid
    
#기기조회
def getDevice(uuid):
    sql = f"SELECT uuid,name,creation_time,expiration_time,is_expired FROM rdms_devices WHERE uuid=%s;"
    cursor.execute(sql,(uuid,))
    result = cursor.fetchall()
    if(len(result)==0):
        return {}
    else:
        result = result[0]
        deviceData = {
            "uuid":result[0],
            "name":result[1],
            "creation_time":result[2],
            "expiration_time":result[3],
            "is_expired":result[4]
            }
        return deviceData

#모든 기기 정보 가져오기
def getAllDevices():
    sql = f"SELECT uuid,name,creation_time,expiration_time,is_expired FROM rdms_devices;"
    cursor.execute(sql)
    results = cursor.fetchall()
    if(len(results)==0):
        return []
    else:
        data = [{
            "uuid":result[0],
            "name":result[1],
            "creation_time":result[2],
            "expiration_time":result[3],
            "is_expired":result[4]
            } for result in results]
        return data

#기기추가
def addDevice(otpData):
    uuid = GenerateUUID()
    sql = f"INSERT INTO rdms_devices (uuid,name) VALUES (%s,%s);"
    cursor.execute(sql,(uuid,otpData["name"]))
    db.commit()
    return getDevice(uuid)

#기기삭제
def deleteDevice(otpData):
    admin = otpData["admin"]
    if isRoot(admin):
        uuid = otpData["uuid"]
        if len(getDevice(uuid))==0:
            return False
        else:
            sql = f"DELETE FROM rdms_devices WHERE uuid=%s;"
            cursor.execute(sql,(uuid,))
            db.commit()
            return True
    else:
        return False
        