from flask import Flask, request, render_template
import json, urllib, os

app = Flask(__name__)

@app.route("/")  #設定根目錄
def home():  #連到根目錄要執行的行為
    return render_template("form.html")

@app.route("/aml", methods = ["POST"])
def aml():
    data = {
        "Inputs": {
            "input1": [{
                "Pregnancies": 0,
                "Glucose": request.values["glucose"],
                "BloodPressure": request.values["blood_pressure"],
                "SkinThickness": 35,
                "Insulin": request.values["insulin"],
                "BMI": request.values["bmi"],
                "DiabetesPedigreeFunction": 2.288,
                "Age": request.values["age"],
                "Outcome": 1
            }]
        },
        "GlobalParameters": {}
    }
    body = str.encode(json.dumps(data))
    url = "http://7ac69e26-f176-43dc-b695-668fd9800c4b.eastasia.azurecontainer.io/score"
    api_key = os.environ.get("AML_API_KEY")
    headers =  {"Content-Type": "application/json",
        "Authorization": ("Bearer " + api_key)}
    req = urllib.request.Request(url, body, headers)
    htmlstr = "<html><body><h2>Diabetes Prediction Result</h2>"

    try:
        response = urllib.request.urlopen(req)
        result = json.loads(response.read())
        htmlstr = htmlstr + "結果為"
        if str(result["Results"]["WebServiceOutput0"][0]["Scored Labels"]) == "0.0":
            htmlstr = htmlstr + ": 您沒有糠尿病</body></html>"
        else:
            htmlstr = htmlstr + ": 您有糠尿病</body></html>"
    except urllib.error.HTTPError as error:
        print(f"The request failed {error.code}")
        print(error.info())
        print(json.loads(error.read().decode("utf8", "ignore")))
    
    return htmlstr

@app.route("/<name>")
def hello(name):
    return "Hello, " + name + ". How are you?"

@app.route("/about")
def about():  #連到.../about 要執行的行為
    return "About"

if __name__ == "__name__":  #只在flask框架啟動時執行
    app.run()