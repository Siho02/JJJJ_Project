from flask.json import jsonify
from flask import Flask, render_template, request,url_for

=======
from flask import Flask, render_template, request,url_for
from flask import current_app as current_app
>>>>>>> Stashed changes

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


if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")