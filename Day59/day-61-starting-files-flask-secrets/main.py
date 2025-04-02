from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(),Email()])
    password = PasswordField(label="Password",validators=[DataRequired(),Length(min=8)])
    button = SubmitField(label="Submit")
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = "Hello"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods = ["POST","GET"])
def login():
    my_form = MyForm()
    if my_form.validate_on_submit() == True:
        if my_form.email.data == "admin@gmail.com" and my_form.password.data == "12345678":
            return render_template("success.html")
        return render_template("denied.html")
    
    return render_template("login.html",form = my_form)
if __name__ == '__main__':
    app.run(debug=True)
