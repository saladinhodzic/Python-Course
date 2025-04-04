from flask import Flask,render_template,request

app = Flask(__name__)

articles = {}

@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        articles[request.form.get("local")] = f"{request.form.get("kolicina")} {request.form.get("vrsta")} {request.form.get("artikl")}"
        print(articles)
        
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)