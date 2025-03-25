from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    data=response.json()
    return render_template("index.html",name = data["name"],gender=data['gender'],percentage=data['probability'])
@app.route("/blog")
def blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("blog.html",data=data)
if __name__ == "__main__":
    app.run(debug=True)