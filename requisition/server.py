from flask import Flask,render_template,request
from datetime import datetime,timedelta

date = str(datetime.now().date() + timedelta(days=1))
month = date.split("-")[1]
day = date.split("-")[2]
premija_pattern = f"PRM-{day}{month}-ORD456"
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
        vrsta = request.form.get("vrsta")
        if local not in articles:
            articles[local] = {}
        articles[local][artikl] = f"{kolicina}x {vrsta}"
    return render_template("premija.html",articles=articles,order = premija_pattern)
if __name__ == "__main__":
    app.run(debug=True)