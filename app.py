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


@app.route('/employees', methods=["POST", "GET"])
def employees():
    """
    Render the employees page of the application.
    """
    data = None
    # Populate table with employees from database
    if request.method == "GET":
        query = "SELECT * FROM Employees"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        cur.close()

    # Add a new employee
    elif request.method == "POST":
        employee_name = request.form['employee_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        current = True if request.form.get('current') == '1' else False
        if employee_name and phone_number and email and current:
            query = "INSERT INTO Employees (employee_name, phone_number, email, current) VALUES (%s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (employee_name, phone_number, email, current))
            mysql.connection.commit()
            cur.close()
            return redirect('/employees')

    if data is None:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Employees")
        data = cur.fetchall()
        cur.close()

    return render_template('employees.html', data=data, year=year)

# Todo: Delete Employee

# Todo: Edit Employee


@app.route('/menu', methods=["POST", "GET"])
def menu():
    """
    Render the menu page of the application.
    """
    data = None
    # Populate table with menu items from database
    if request.method == "GET":
        query = "SELECT * FROM MenuItems"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        cur.close()

    # Add a new menu item
    elif request.method == "POST":
        dish_name = request.form['dish_name']
        price = request.form['price']
        description = request.form['description']
        category = request.form.get('category')
        current = True if request.form.get('current') == '1' else False
        if dish_name and price and category and current:
            query = "INSERT INTO MenuItems (dish_name, price, description, category, current) VALUES (%s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (dish_name, price, description, category, current))
            mysql.connection.commit()
            cur.close()
            return redirect('/menu')

    if data is None:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Menu")
        data = cur.fetchall()
        cur.close()

    return render_template('menu.html', data=data, year=year)


@app.route('/orders',  methods=["POST", "GET"])
def orders():
    """
    Render the orders page of the application.
    """
    data = None
    # Populate table with orders from database
    if request.method == "GET":
        query = """
        SELECT 
            Orders.order_id,
            Customers.customer_name,
            Employees.employee_name,
            Orders.order_date,
            Orders.status,
            Orders.total_amount
        FROM 
            Orders
        JOIN 
            Customers ON Orders.customer_id = Customers.customer_id
        JOIN 
            Employees ON Orders.employee_id = Employees.employee_id
        """
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        cur.close()

        for order in data:
            if order['order_date']:
                order['order_date'] = order['order_date'].strftime('%Y-%m-%d')

    return render_template('orders.html', data=data, year=year)


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
