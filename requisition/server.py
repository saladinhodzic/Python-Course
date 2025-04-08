from flask import Flask,render_template,request
from datetime import datetime,timedelta

date = str(datetime.now().date() + timedelta(days=1))
month = date.split("-")[1]
day = date.split("-")[2]
with open("premija_order.txt",'r+') as order:
    ord = int(order.read()) + 1
    premija_pattern = f"PRM-{day}{month}-ORD{ord}"
    order.seek(0)
    order.write(str(ord))
app = Flask(__name__)

articles = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/premija",methods=["POST","GET"])
def premija():
    if request.method == "POST":
        local = request.form.get("local").title()
        artikl = request.form.get("artikl").title()
        kolicina = request.form.get("kolicina")
        if local not in articles:
            articles[local] = {}
        articles[local][artikl] = f"{kolicina}"
    return render_template("premija.html",articles=articles,order = premija_pattern)
if __name__ == "__main__":
    app.run(debug=True)