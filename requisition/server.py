from flask import Flask,render_template,request,redirect,url_for
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user
from datetime import datetime,timedelta
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired

# user class
class User(UserMixin):
    def __init__(self,id):
        self.id = id

# form
class MyForm(FlaskForm):
    input = StringField("Ime radnje: ",validators=[DataRequired("Obavezan unos")])
    password = PasswordField("Unesite lozinku: ",validators=[DataRequired("Obavezan unos")])
    submit = SubmitField("Potvrdi",render_kw={'class':'btn'})
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
    
# settings for app
app = Flask(__name__)
app.secret_key = "sendvicgalerija"
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(id):
    return User(id)

articles = {}

@app.route("/")
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('auth'))
    return render_template('index.html')

@app.route("/premija",methods=["POST","GET"])
@login_required
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
            user = User(id="saladin")
            login_user(user)
            return redirect(url_for("home"))
    return render_template("auth.html", form = form)
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)