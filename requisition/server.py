from flask import Flask,render_template,request,redirect,url_for
from datetime import datetime,timedelta
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    input = StringField("Ime radnje: ",validators=[DataRequired("Obavezan unos")])
    password = PasswordField("Unesite lozinku: ",validators=[DataRequired("Obavezan unos")])
    submit = SubmitField("Potvrdi")
# tracking order date
date = str(datetime.now().date() + timedelta(days=1))
month = date.split("-")[1]
day = date.split("-")[2]
# tracking order number
with open("premija_order.txt",'r+') as order:
    ord = int(order.read()) + 1
    premija_pattern = f"PRM-{day}{month}-ORD{ord}"
    order.seek(0)
    order.write(str(ord))
    
    
app = Flask(__name__)
app.secret_key = "sendvicgalerija"
articles = {}

@app.route("/")
def home():
    return redirect(url_for('auth'))

@app.route("/premija",methods=["POST","GET"])
def premija():
    if request.method == "POST":
        local = request.form.get("local").title()
        artikl = request.form.get("artikl").title()
        kolicina = request.form.get("kolicina")
        if local not in articles:
            articles[local] = {}
        articles[local][artikl] = f"{kolicina}"
    return render_template("premija.html",articles=articles,order = premija_pattern)

@app.route("/auth",methods= ["POST","GET"])
def auth():
    form = MyForm()
    if form.validate_on_submit() == True:
        if form.input.data == "saladin" and form.password.data == "123456":
            return render_template("index.html")
    return render_template("auth.html", form= form)
if __name__ == "__main__":
    app.run(debug=True)