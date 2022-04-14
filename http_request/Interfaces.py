from flask import Flask

app = Flask(__name__)


@app.route("/index")
def  register():
    return  "hello world"

if __name__ == '__main__':
    app.run(port=8888, debug=True)