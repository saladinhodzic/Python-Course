from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    data=response.json()
    return render_template("index.html",name = data["name"],gender=data['gender'],percentage=data['probability'])

if __name__ == "__main__":
    app.run(debug=True)