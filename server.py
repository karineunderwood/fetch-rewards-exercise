"""Server for Fetching points."""

from flask import (Flask, render_template, request, flash,
                    session, redirect)
import random
from datetime import date
from jinja2 import StrictUndefined
import os


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():

    return render_template('home.html')









if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)