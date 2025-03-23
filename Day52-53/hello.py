from flask import Flask

app = Flask(__name__)

def bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

@app.route("/")
@bold
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)