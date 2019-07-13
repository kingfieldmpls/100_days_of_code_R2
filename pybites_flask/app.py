from flask import Flask, render_template
from data import new_on_netflix


app = Flask(__name__)


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name, new_on_netflix=new_on_netflix)


if __name__ == "__main__":
    app.run()
