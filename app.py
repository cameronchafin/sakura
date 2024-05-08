from flask import Flask, render_template, json, redirect
from flask import request
import datetime
import os


app = Flask(__name__)

year = datetime.date.today().year


# Routes
@app.route('/')
def index():
    """
    Render the homepage of the application.
    """
    return render_template('index.html', year=year)


@app.route('/customers')
def customers():
    """
    Render the customers page of the application.
    """
    return render_template('customers.html', year=year)


@app.route('/employees')
def employees():
    """
    Render the employees page of the application.
    """
    return render_template('employees.html', year=year)


@app.route('/orders')
def orders():
    """
    Render the orders page of the application.
    """
    return render_template('orders.html', year=year)


@app.route('/menu')
def menu():
    """
    Render the menu page of the application.
    """
    return render_template('menu.html', year=year)


# Listener
if __name__ == "__main__":

    #Start the app on port 2398
    app.run(port=2398, debug=True)
