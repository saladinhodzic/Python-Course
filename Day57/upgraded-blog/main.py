from flask import Flask,render_template
import requests

response = requests.get("https://api.npoint.io/d5d7beb7bf4569e08e0b")
data = response.json()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",posts=data)

@app.route("/about-us")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:id>")
def post(id):
    return render_template("post.html",post = data[id-1])

if __name__ == "__main__":
    app.run(debug=True)