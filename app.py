from flask import Flask

app = Flask(__name__)

@app.route("/")  #設定根目錄
def home():  #連到根目錄要執行的行為
    return "Hello, World"

@app.route("/about")
def about():  #連到.../about 要執行的行為
    return "About"

if __name__ == "__name__":  #只在flask框架啟動時執行
    app.run()