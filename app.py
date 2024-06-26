from flask import Flask, render_template, json, redirect, flash
from flask_mysqldb import MySQL
from flask import request
import datetime
import os
import database.db_connector as db
from dotenv import load_dotenv, find_dotenv

# Citation for configuring app and connecting to database:
# Date: 6/8/2024
# Adapted from OSU Flask Starter APP
# https://github.com/osu-cs340-ecampus/flask-starter-app
# All Routes below setup consist of original code based on the 
# required functionality of the application

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


# ---------- Customers ---------- #
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


# ---------- Employees ---------- #
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


# Edit Employee
@app.route('/employees/update', methods=['POST'])
def update_employee():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        employee_name = request.form['employee_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        current = True if request.form.get('current') == '1' else False

        cur = mysql.connection.cursor()
        query = """
        UPDATE Employees
        SET employee_name = %s, phone_number = %s, email = %s, current = %s
        WHERE employee_id = %s
        """
        cur.execute(query, (employee_name, phone_number, email, current, employee_id))
        mysql.connection.commit()
        cur.close()
    return redirect('/employees')


# ---------- Menu ---------- #
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


# Edit Menu Item
@app.route('/menu/update', methods=['POST'])
def update_menu_item():
    if request.method == 'POST':
        item_id = request.form['item_id']
        dish_name = request.form['dish_name']
        price = request.form['price']
        description = request.form['description']
        category = request.form.get('category')
        current = True if request.form.get('current') == '1' else False

        cur = mysql.connection.cursor()
        query = """
        UPDATE MenuItems
        SET dish_name = %s, price = %s, description = %s, category = %s, current = %s
        WHERE item_id = %s
        """
        cur.execute(query, (dish_name, price, description, category, current, item_id))
        mysql.connection.commit()
        cur.close()
    return redirect('/menu')


# ---------- Orders ---------- #
@app.route('/orders', methods=["POST", "GET"])
def orders():
    """
    Render the orders page of the application.
    """
    cur = mysql.connection.cursor()

    # Fetch customers for dropdown
    cur.execute("SELECT customer_id, customer_name FROM Customers")
    customers = cur.fetchall()

    # Fetch only current employees for dropdown
    cur.execute("SELECT employee_id, employee_name FROM Employees WHERE current = 1")
    employees = cur.fetchall()

    # Add an order
    if request.method == "POST":
        customer_id = request.form['customer']
        employee_id = request.form.get('employee')  # Nullable field
        order_date = request.form['date']
        status = request.form.get('status')
        # Initialize total_amount to 0.00 when creating a new order
        total_amount = 0.00

        if customer_id and order_date and status:
            query = """
            INSERT INTO Orders (customer_id, employee_id, order_date, status, total_amount)
            VALUES (%s, %s, %s, %s, %s)
            """
            cur.execute(query, (customer_id, employee_id if employee_id else None, order_date, status, total_amount))
            mysql.connection.commit()
            cur.close()
            return redirect('/orders')

    # Populate table with orders from database
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
    LEFT JOIN 
        Employees ON Orders.employee_id = Employees.employee_id
    """
    cur.execute(query)
    data = cur.fetchall()
    cur.close()

    # Format order date
    for order in data:
        if order['order_date']:
            order['order_date'] = order['order_date'].strftime('%Y-%m-%d')

    return render_template('orders.html', customers=customers, employees=employees, data=data, year=year)


# Edit an Order
@app.route('/orders/update', methods=['POST'])
def update_order():
    order_id = request.form['order_id']
    customer_id = request.form['customer']
    employee_id = request.form.get('employee')
    order_date = request.form['date']
    status = request.form['status']

    if customer_id and order_date and status:
        query = """
        UPDATE Orders
        SET customer_id = %s, employee_id = %s, order_date = %s, status = %s
        WHERE order_id = %s
        """
        cur = mysql.connection.cursor()
        cur.execute(query, (customer_id, employee_id if employee_id else None, order_date, status, order_id))
        mysql.connection.commit()
        cur.close()

    return redirect('/orders')


# ---------- Order Details ---------- #
@app.route('/order_details', methods=["POST", "GET"])
def order_details():
    """
    Render the order details page of the application.
    """
    cur = mysql.connection.cursor()

    # Fetch existing orders and menu items for dropdowns
    cur.execute("""
    SELECT Orders.order_id, Customers.customer_name, Orders.order_date
    FROM Orders
    JOIN Customers ON Orders.customer_id = Customers.customer_id
    ORDER BY Orders.order_date DESC
    """)
    orders = cur.fetchall()

    cur.execute("SELECT item_id, dish_name FROM MenuItems")
    menu_items = cur.fetchall()

    # Add an order detail
    if request.method == "POST":
        order_id = request.form['order_id']
        item_id = request.form['item_id']
        quantity = request.form['quantity']
        # Fetch the price of the selected menu item
        cur.execute("SELECT price FROM MenuItems WHERE item_id = %s", (item_id,))
        item_price = cur.fetchone()['price']
        # Calculate subtotal for the entered quantity
        subtotal = float(item_price) * int(quantity)

        if order_id and item_id and quantity and item_price:
            insert_query = """
            INSERT INTO OrderDetails (order_id, item_id, quantity, price)
            VALUES (%s, %s, %s, %s)
            """
            cur.execute(insert_query, (order_id, item_id, quantity, item_price))
            mysql.connection.commit()

            # Update total amount in Orders table
            cur.execute("""
                UPDATE Orders 
                SET total_amount = total_amount + %s 
                WHERE order_id = %s
            """, (float(item_price) * int(quantity), order_id))
            mysql.connection.commit()

        cur.close()
        return redirect('/order_details')

    # Populate table with order details from database
    query = """
    SELECT 
        OrderDetails.order_detail_id,
        Customers.customer_name,
        Orders.order_date,
        MenuItems.dish_name AS menu_item,
        OrderDetails.price,
        OrderDetails.quantity,
        (OrderDetails.price * OrderDetails.quantity) AS subtotal
    FROM 
        OrderDetails
    JOIN 
        Orders ON OrderDetails.order_id = Orders.order_id
    JOIN 
        Customers ON Orders.customer_id = Customers.customer_id
    JOIN 
        MenuItems ON OrderDetails.item_id = MenuItems.item_id
    """
    cur.execute(query)
    details = cur.fetchall()
    cur.close()

    # Format order date
    for detail in details:
        if detail['order_date']:
            detail['order_date'] = detail['order_date'].strftime('%Y-%m-%d')

    return render_template('order_details.html', orders=orders, menu_items=menu_items, details=details, year=year)


# Delete an Order Detail
@app.route('/order_details/delete', methods=['POST'])
def delete_order_detail():
    order_detail_id = request.form.get('order_detail_id')
    if order_detail_id:
        cur = mysql.connection.cursor()

        # Fetch price, quantity, and id for order detail to be deleted
        cur.execute("""
            SELECT price, quantity, order_id 
            FROM OrderDetails 
            WHERE order_detail_id = %s
        """, (order_detail_id,))
        detail = cur.fetchone()

        # calculate amount to be subtracted from order total
        price = detail['price']
        quantity = detail['quantity']
        order_id = detail['order_id']
        amount_to_subtract = float(price) * int(quantity)

        # Delete order detail
        query = "DELETE FROM OrderDetails WHERE order_detail_id = %s"
        cur.execute(query, (order_detail_id,))

        # Update total amount in Orders table
        cur.execute("""
            UPDATE Orders 
            SET total_amount = total_amount - %s 
            WHERE order_id = %s
        """, (amount_to_subtract, order_id))

        mysql.connection.commit()
        cur.close()
    return redirect('/order_details')


@app.route('/order_details/update', methods=['POST'])
def update_order_detail():
    if request.method == 'POST':
        order_detail_id = request.form['order_detail_id']
        item_id = request.form['item_id']
        quantity = request.form['quantity']
        
        cur = mysql.connection.cursor()

        # Fetch the price of the selected menu item
        cur.execute("SELECT price FROM MenuItems WHERE item_id = %s", (item_id,))
        item_price = cur.fetchone()['price']
        # Calculate new subtotal for the entered quantity
        new_subtotal = float(item_price) * int(quantity)

        # Fetch the old price and quantity for the order detail
        cur.execute("""
            SELECT price, quantity, order_id 
            FROM OrderDetails 
            WHERE order_detail_id = %s
        """, (order_detail_id,))
        old_detail = cur.fetchone()
        old_subtotal = float(old_detail['price']) * int(old_detail['quantity'])
        order_id = old_detail['order_id']

        # Update order detail
        update_query = """
        UPDATE OrderDetails
        SET item_id = %s, quantity = %s, price = %s
        WHERE order_detail_id = %s
        """
        cur.execute(update_query, (item_id, quantity, item_price, order_detail_id))

        # Update total amount in Orders table
        cur.execute("""
            UPDATE Orders 
            SET total_amount = total_amount - %s + %s
            WHERE order_id = %s
        """, (old_subtotal, new_subtotal, order_id))

        mysql.connection.commit()
        cur.close()

    return redirect('/order_details')


# Listener
if __name__ == "__main__":

    #Start the app on port 2398
    app.run(port=2398, debug=True)
