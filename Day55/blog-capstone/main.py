from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/9174b947efdd3c710458")
    data = response.json()
    return render_template("index.html",data=data)

@app.route("/post/<int:id>")
def get_post(id):
    response = requests.get("https://api.npoint.io/9174b947efdd3c710458")
    data = response.json()
    return render_template("post.html",post = data[id-1])

if __name__ == "__main__":
    app.run(debug=True)
