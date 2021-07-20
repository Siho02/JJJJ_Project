from flask import Flask, render_template, request,url_for
from flask import current_app as current_app

app = Flask(__name__)


@app.route('/', methods=["GET"])
def basic():
    return render_template('index.html')
    
@app.route("/search", methods=["get"])
def search():
    return render_template("elements.html")

@app.route("/info", methods=["get"])
def chart():
    return render_template("generic.html")

@app.route("/info2", methods=["get"])
def chart2():
    return render_template("generic2.html")

@app.route("/info3", methods=["get"])
def chart3():
    return render_template("generic3.html")



if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
