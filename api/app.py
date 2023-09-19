from flask import Flask, request, abort
from flask_cors import CORS
import DB

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': '*'}})

#배포 주소 및 포트
host_addr = "0.0.0.0"
host_port = 5000

#로그인기능
@app.route("/api/auth/login",methods=['POST'])
def login():
    body = request.get_json()
    if "username" in body and "password" in body:
        if DB.loginAuth(body["username"],body["password"]):
            return {"message":"Success","data":{}}
        else:
            abort(401)
    else:
        abort(400)

if __name__ == "__main__":
    app.run(debug=True,
            host=host_addr,
            port=host_port)