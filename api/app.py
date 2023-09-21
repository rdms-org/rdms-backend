from flask import Flask, request, abort, session, redirect
from flask_cors import CORS
import DB
from dotenv import load_dotenv
import os
#환경변수 로드
load_dotenv()

#Flask 앱 생성 및 설정
app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET_KEY')
CORS(app, resources={r'*': {'origins': '*'}})

#배포 주소 및 포트
host_addr = "0.0.0.0"
host_port = 5000

#응답 형식 반환
def response_format(msg,data={}):
        return {"message":msg,"data":data}


#로그인 기능
@app.route("/api/auth/login",methods=['POST'])
def login():
    body = request.get_json()
    if "username" in body and "password" in body:
        username = body["username"]
        password = body["password"]

        if DB.loginAuth(username, password):
            session["username"] = username
            return response_format("success")
        else:
            abort(401)
    else:
        abort(400)

#세션 검사 기능
@app.route("/api/auth/valid",methods=['GET'])
def valid(): 
    if "username" in session: 
        return response_format("success")
    else:
        return abort(401)


        
    

if __name__ == "__main__":
    app.run(debug=True,
            host=host_addr,
            port=host_port)