from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    try:
        articles = {}
        store_name = request.form.get("radnja")
        if store_name not in articles:
            articles[store_name] = {}
        need = request.form.get("artikl")
        quantity = request.form.get("kolicina")
        articles[store_name][need] = quantity
    except KeyError as e:
        print(e)
    return render_template("index.html",articles = articles)

if __name__ == "__main__":
    app.run(debug=True)