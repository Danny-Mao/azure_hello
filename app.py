from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")  #設定根目錄
def home():  #連到根目錄要執行的行為
    return render_template("form.html")

@app.route("/<name>")  #角括號內可取任意名稱(變數名稱規則)
def hello(name):  #參數同上一行角括號內
    return "Hello, " + name + ". How are you?"

@app.route("/about")
def about():  #連到.../about 要執行的行為
    return "About"

if __name__ == "__name__":  #只在flask框架啟動時執行
    app.run()