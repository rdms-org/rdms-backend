from flask import Flask, request, abort, session
from flask_cors import CORS
import DB
import os
import OTP

#Flask 앱 생성 및 설정
app = Flask(__name__)
app.secret_key = os.urandom(24)

#개발환경에서만 사용
CORS(app, resources={r'*': {'origins': '*'}})

#배포 주소 및 포트
host_addr = "0.0.0.0"
host_port = 5000

#응답 형식 반환
def response_format(msg,data={}):
        resp = {"message":msg,"data":data}
        return resp


#세션 검사 기능
@app.route("/api/auth/valid",methods=['GET'])
def valid(): 
    if "username" in session: 
        data = DB.getUser(session["username"])
        return response_format("Success",data)
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
            data = DB.getUser(username)
            return response_format("Success",data)
        else:
            return response_format("Fail")
    else:
        abort(400)

#로그아웃 기능
@app.route("/api/auth/logout",methods=['GET'])
def logout(): 
    if "username" in session: 
        session.clear()
        return response_format("Success")
    else:
        return abort(401)

#OTP 생성
@app.route("/api/auth/otp/gen",methods=['POST'])
def gen_otp(): 
    if "username" in session: 
        body = request.get_json()
        if "type" in body and "data" in body:
            type = body["type"]
            data = body["data"]
            otp = OTP.generate(type, data)
            return response_format("Success", otp)
        else:
            return abort(400)
    else:
        return abort(401)

#otp 인증
@app.route("/api/auth/otp/valid",methods=['POST'])
def valid_otp():
    body = request.get_json()
    if "otp" in body:
        otp = body["otp"]
        if "uuid" in body:
            uuid = body["uuid"]
            result = OTP.valid(otp,uuid)
        else:
            result = OTP.valid(otp)
        if result:
            return response_format("Success",result)
        else:
            return response_format("Fail")
    else:
        return abort(400)

#otp 작업 실행
@app.route("/api/auth/otp/execute",methods=['POST'])
async def execute_otp():
    if "username" in session: 
        body = request.get_json()
        if "otp" in body:
            otp = body["otp"]
            result = await OTP.execute(otp)
            if result:
                return response_format("Success",result)
            else:
                return response_format("Fail")
        else:
            return abort(400)
    else:
        return abort(401)

#otp 만료
@app.route("/api/auth/otp/expire",methods=['POST'])
def expire_otp():
    if "username" in session: 
        body = request.get_json()
        if "otp" in body:
            otp = body["otp"]
            result = OTP.expire(otp)
            if result:
                return response_format("Success")
            else:
                return response_format("Fail")
        else:
            return abort(400)
    else:
        return abort(401)

#모든 디바이스 정보 가져오기
@app.route("/api/devices",methods=['GET'])
def get_all_devices():
    if "username" in session: 
        res = DB.getAllDevices()
        return response_format("Success",res)
    else:
        return abort(401)

#특정 디바이스 정보 가져오기
@app.route("/api/device",methods=['GET'])
def get_device():
    if "username" in session: 
        args = request.args.to_dict()
        #todo
    else:
        return abort(401)

if __name__ == "__main__":
    app.run(debug=True,
            host=host_addr,
            port=host_port)