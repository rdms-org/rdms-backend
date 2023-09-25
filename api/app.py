from flask import Flask, request, abort, session
from flask_cors import CORS
import DB
import os
import random
import time

#Flask 앱 생성 및 설정
app = Flask(__name__)
app.secret_key = os.urandom(24)

#개발환경에서만 사용
CORS(app, resources={r'*': {'origins': '*'}})

#배포 주소 및 포트
host_addr = "0.0.0.0"
host_port = 5000

#otp 작업 저장해둘 딕셔너리, key = otp, value = info
otp_list = {}

#응답 형식 반환
def response_format(msg,data={}):
        return {"message":msg,"data":data}


#세션 검사 기능
@app.route("/api/auth/valid",methods=['GET'])
def valid(): 
    if "username" in session: 
        return response_format("Success")
    else:
        return response_format("Fail")

#로그인 기능
@app.route("/api/auth/login",methods=['POST'])
def login():
    body = request.get_json()
    if "username" in body and "password" in body:
        username = body["username"]
        password = body["password"]

        if DB.loginAuth(username, password):
            session["username"] = username
            return response_format("Success")
        else:
            return response_format("Fail")
    else:
        abort(400)

#로그아웃 기능
@app.route("/api/auth/logout",methods=['POST'])
def logout(): 
    if "username" in session: 
        session.clear()
        return response_format("Success")
    else:
        return abort(401)

@app.route("/api/auth/otp/gen",methods=['GET'])
def get_otp(): 
    if "username" in session: 
        body = request.get_json()
        if "type" in body and "data" in body:
            type = body["type"]
            data = body["data"]
            while True:
                otp = random.randint(0,9999)
                if otp not in otp_list:
                    break
            otp_info = {"expires":time.time()+180,"type":type,"data":data}
            otp_list[otp] = otp_info
            return response_format("Success",{"otp":otp})
        else:
            return abort(400)
    else:
        return abort(401)


if __name__ == "__main__":
    app.run(debug=True,
            host=host_addr,
            port=host_port)