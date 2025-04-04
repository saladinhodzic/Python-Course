from flask import Flask,render_template,request

app = Flask(__name__)

articles = {}

@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        local = request.form.get("local")
        artikl = request.form.get("artikl")
        kolicina = request.form.get("kolicina")
        vrsta = request.form.get("vrsta")
        if local not in articles:
            articles[local] = {}
        articles[local][artikl] = f"{kolicina}x {vrsta}"
    return render_template("index.html",articles=articles)
if __name__ == "__main__":
    app.run(debug=True)