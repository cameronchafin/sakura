from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import datetime
import os
import database.db_connector as db
from dotenv import load_dotenv, find_dotenv


db_connection = db.connect_to_database()

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get("340DBHOST")
app.config['MYSQL_USER'] = os.environ.get("340DBUSER")
app.config['MYSQL_PASSWORD'] = os.environ.get("340DBPW")
app.config['MYSQL_DB'] = os.environ.get("340DB")
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

year = datetime.date.today().year


# Routes
@app.route('/')
def index():
    """
    Render the homepage of the application.
    """
    return render_template('index.html', year=year)


@app.route('/customers', methods=["POST", "GET"])
def customers():
    """
    Render the customers page of the application.
    """
    data = None

    # Populate table with customers from database
    if request.method == "GET":
        query = "SELECT * FROM Customers"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        cur.close()

    # Add a new customer
    elif request.method == "POST":
        customer_name = request.form["customer_name"]
        phone_number = request.form["phone_number"]
        email = request.form["email"]
        if customer_name and phone_number and email:
            query = "INSERT INTO Customers (customer_name, phone_number, email) VALUES (%s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (customer_name, phone_number, email))
            mysql.connection.commit()
            cur.close()
            return redirect('/customers')

    if data is None:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Customers")
        data = cur.fetchall()
        cur.close()

    return render_template('customers.html', data=data, year=year)


# Delete a customer
@app.route('/customers/delete', methods=['POST'])
def delete_customer():
    customer_id = request.form.get('customer_id')
    if customer_id:
        query = "DELETE FROM Customers WHERE customer_id = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (customer_id))
        mysql.connection.commit()
        cur.close()
    return redirect('/customers')


# Edit customer
@app.route('/customers/update', methods=['POST'])
def update_customer():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        customer_name = request.form['customer_name']
        phone_number = request.form['phone_number']
        email = request.form['email']

        cur = mysql.connection.cursor()
        query = """
        UPDATE Customers
        SET customer_name = %s, phone_number = %s, email = %s
        WHERE customer_id = %s
        """
        cur.execute(query, (customer_name, phone_number, email, customer_id))
        mysql.connection.commit()
        cur.close()
    return redirect('/customers')


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


@app.route('/order_details')
def order_details():
    """
    Render the order details page of the application.
    """
    return render_template('order_details.html', year=year)


# Listener
if __name__ == "__main__":

    #Start the app on port 2398
    app.run(port=2398, debug=True)
