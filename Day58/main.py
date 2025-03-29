# HTML Forms - catching submitted form via Flask server
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    return f"{request.form["name"]}:{request.form["password"]}"

if __name__ == "__main__":
    app.run(debug=True)