from flask import Flask

app = Flask(__name__)
host_addr = "0.0.0.0"
host_port = 8080

@app.route('/')
def hello():
    return "rdms test, try /ping!"

@app.route('/ping')
def ping():
    return {'response': 'pong'}


if __name__ == "__main__":
    app.run(debug=True,
            host=host_addr,
            port=host_port)