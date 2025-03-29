from flask import Flask, render_template,request
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv(".env")
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact",methods=["POST","GET"])
def recieve_data():
    if request.method == "POST":
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=os.getenv("EMAIL"),password=os.getenv("PASSWORD"))
            connection.sendmail(from_addr=os.getenv("EMAIL"),to_addrs=os.getenv("TO"),msg=f"Subject:New User\n\nName:{request.form["name"]}\nEmail:{request.form["email"]}\nPhone:{request.form["phone"]}")
        return render_template("contact.html",text = True)
    else:
        return render_template("contact.html", text = False)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
