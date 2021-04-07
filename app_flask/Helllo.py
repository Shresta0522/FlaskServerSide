from flask import Flask,render_template
import datetime
app=Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Hello</h1'

# @app.route("/")
# def index():
#     return "Hello World!!"


# @app.route('/<name>')
# def index(name):
#     return '<h1> Hello {}!</h1>'.format(name)

# if __name__ == '__main__':
#     app.run()

# Capitalize
# @app.route("/<string:name>")
# def hello(name):
#     name=name.capitalize()
#     return f"<h1>Hello, {name}!</h1>"


# @app.route("/")
# def index():
#     headline="HELLO!!!"
#     return render_template("index.html ",headline=headline)



# @app.route("/")
# def index():
#     now=datetime.datetime.now()
#     new_year=now.month==1 and now.day==1
#     return render_template("index.html ",new_year=new_year)



# for loop implentation
# @app.route("/")
# def index():
#     names=["Danny","Bob","Charlie"]

#     return render_template("index.html ",names=names)



