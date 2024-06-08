-- This file features data manipulation queries that match those
-- found in the server-side code for the various routes in the application

------- CUSTOMERS TABLE -------

-- get data for all customers
SELECT *
FROM Customers;

-- insert / add new customer into the database
INSERT INTO Customers (
    customer_name,
    phone_number,
    email
)
VALUES (
    :customer_name_input,
    :phone_number_input,
    :email_input
);


-- update customer based on customer_id
UPDATE Customers
SET customer_name = :customer_name_input,
    phone_number = :phone_number_input,
    email = :email_input
WHERE customer_id = :customer_id_input;



------- EMPLOYEES TABLE -------

-- get data for all employees
SELECT *
FROM Employees;

-- insert / add a new employee into the database
INSERT INTO Employees (
    employee_name,
    phone_number,
    email,
    current
)
VALUES (
    :employee_name_input,
    :phone_number_input,
    :email_input,
    :current_status
);

-- update employee base on employee_id
UPDATE Employees
SET employee_name = :employee_name_input,
    phone_number = :phone_number_input,
    email = :email_input,
    current = :current_input
WHERE employee_id = :employee_id_input;



------- ORDERS TABLE -------

-- fetch customers for dropdown
SELECT customer_id, customer_name FROM Customers;

-- fetch only current employees for dropdown
SELECT employee_id, employee_name FROM Employees WHERE current = 1;

-- get data for all orders
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
    Employees ON Orders.employee_id = Employees.employee_id;


-- insert / add new order into the database
INSERT INTO Orders (
    customer_id,
    employee_id,
    order_date,
    status,
    total_amount
)
VALUES (
    :customer_id_input,
    :employee_id_input,  -- Nullable field
    :order_date_input,
    :status_input,
    :total_amount_input
);

-- update order based on order_id
UPDATE Orders
SET customer_id = :customer_id_input,
    employee_id = :employee_id_input,  -- Nullable field
    order_date = :order_date_input,
    status = :status_input
WHERE order_id = :order_id_input;



------- MENU ITEMS TABLE -------

-- select all menu items currently available
SELECT *
FROM MenuItems;

-- insert a new menu item into the database
INSERT INTO MenuItems (
    dish_name,
    price,
    description,
    category,
    current
)
VALUES (
    :dish_name_input,
    :price_input,
    :description_input,
    :category_input,
    :current_input
);

-- update menu item based on item_id
UPDATE MenuItems
SET dish_name = :dish_name_input,
    price = :price_input,
    description = :description_input,
    category = :category_input,
    current = :current_input
WHERE item_id = :item_id_input;



------- ORDER DETAILS TABLE -------

-- fetch existing orders for dropdown
SELECT Orders.order_id, Customers.customer_name, Orders.order_date
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id
ORDER BY Orders.order_date DESC;

-- fetch all menu items for dropdown
SELECT item_id, dish_name FROM MenuItems;

-- get data for all order details
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
    MenuItems ON OrderDetails.item_id = MenuItems.item_id;

-- insert / add new order detail into the database
INSERT INTO OrderDetails (
    order_id,
    item_id,
    quantity,
    price
)
VALUES (
    :order_id_input,
    :item_id_input,
    :quantity_input,
    :price_input
);

-- update total amount in Orders table after adding order detail
UPDATE Orders 
SET total_amount = total_amount + :subtotal_input
WHERE order_id = :order_id_input;

-- update order detail based on order_detail_id
UPDATE OrderDetails
SET item_id = :item_id_input, 
    quantity = :quantity_input, 
    price = :price_input
WHERE order_detail_id = :order_detail_id_input;

-- update total amount in Orders table after updating order detail
UPDATE Orders 
SET total_amount = total_amount - :old_subtotal_input + :new_subtotal_input
WHERE order_id = :order_id_input;

-- delete order detail based on order_detail_id
DELETE FROM OrderDetails 
WHERE order_detail_id = :order_detail_id_input;

-- update total amount in Orders table after deleting order detail
UPDATE Orders 
SET total_amount = total_amount - :amount_to_subtract_input 
WHERE order_id = :order_id_input;