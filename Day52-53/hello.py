from flask import Flask

app = Flask(__name__)

def bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper
@app.route("/")
@bold
@emphasis
@underlined
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)