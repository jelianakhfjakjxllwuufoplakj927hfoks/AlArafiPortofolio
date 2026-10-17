from flask import Flask, redirect, render_template
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(HTTPException)
def handle_http_error(error):
    return redirect("/")

@app.errorhandler(Exception)
def handle_error(error):
    app.logger.exception("Internal server error")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
