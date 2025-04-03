from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    store_name = request.form.get("radnja")
    return render_template("index.html",store = store_name)

if __name__ == "__main__":
    app.run(debug=True)