from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/login",methods = ["POST"])
def recieve_data():
    pass
if __name__ == "__main__":
    app.run(debug=True)