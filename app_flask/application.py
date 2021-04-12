from flask import Flask,render_template,request
import datetime

app=Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/Register", methods=["GET", "POST"])
def Register():
    name = request.form.get('name')
    return render_template("Register.html",name=name)


# @app.route("/index",methods=["POST"])
# def index():
#     name=request.form.get("name")
#     return render_template("index.html",name=name)

# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         uname = request.form['uname']
#         mail = request.form['mail']
#         passw = request.form['passw']


#         # return redirect(url_for("login"))
#     return render_template("i.html")


if __name__ == '__main__':
    app.run(debug=True)