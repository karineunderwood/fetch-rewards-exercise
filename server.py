"""Server for Fetching points."""

from flask import (Flask, render_template, request, flash,
                    session, redirect)
import random
from datetime import datetime
from jinja2 import StrictUndefined
import os


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

TRANSACTIONS = []

@app.route("/")
def show_homepage():

    return render_template("base.html")

@app.route("/add-transactions")
def show_options_to_add_points():
    "Show form to enter points to add."

    return render_template("add-transactions.html")

@app.route("/add-transactions", methods=["POST"])
def add_transactions():
    """This is the route to add points from payers. """
    if request.method == "POST":

        payer = request.form.get("Payer")
        points = request.form.get("Points") 

        transaction = {"Payer": payer.upper(), "Point": int(points), "Timestamp": datetime.now()}
        TRANSACTIONS.append(transaction)

    

        print(TRANSACTIONS)
        

    return render_template("add-transactions.html")

    
@app.route("/spend-points")
def spend_points():
    """This route shows form to spend points."""

    return render_template("spend-points.html")

@app.route("/spend-points", methods=["POST"])
def store_points():
    """This allows users to request points to spend."""
    history_of_payers = []
    # if request.method == "POST":
    points_requested = request.form.get("Points-spend")
    points_requested = int(points_requested)
    
    for i in range(len(TRANSACTIONS)):
        if TRANSACTIONS[i]["Point"] >= points_requested:
            TRANSACTIONS[i]["Point"] -= points_requested
            history_of_payers.append({"Payer": TRANSACTIONS[i]["Payer"], "Points": -points_requested})
            break
        else:
            points_requested -= TRANSACTIONS[i]["Point"]
            history_of_payers.append({"Payer": TRANSACTIONS[i]["Payer"], "Points": -TRANSACTIONS[i]["Point"]})
            TRANSACTIONS[i]["Point"] = 0
    print(history_of_payers)
    print(TRANSACTIONS)
        

        
    return render_template("spend-points.html")
        
@app.route("/show-balance")
def show_balance():

    remainder_balance = {}

    for i in TRANSACTIONS:
        remainder_balance[i["Payer"]] = i["Point"]

    return render_template("show-balance.html", remainder_balance=remainder_balance)    



    

    



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)