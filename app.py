from flask import Flask

app = Flask(__name__)

@app.route("/")  #設定根目錄
def home():  #連到根目錄要執行的行為
    return "Hello, World"

@app.route("/<name>")
def hello(name):
    return "Hello, " + name + ". How are you?"

@app.route("/about")
def about():  #連到.../about 要執行的行為
    return "About"

@app.route("/test1")
def html_test():
    return """
        <!DOCTYPE html>
        <head>
            <title>myweb</title>
        </head>
        <body>
            test web <input>
        </body>
    """

if __name__ == "__name__":  #只在flask框架啟動時執行
    app.run()