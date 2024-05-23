
--CUSTOMERS TABLE

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


-- update customers phone number and email based on customer_id
UPDATE Customers
SET phone_number = :phone_number_input,
    email = :email_input
WHERE customer_id = :customer_id_input;



--EMPLOYEES TABLE

-- this provides the information of all Employees who are currently employed at the company.
SELECT *
FROM Employees
WHERE Current = 1;

-- this allows to insert / add a new employee into the employees table
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

-- update the employees working status
UPDATE Employees
SET current = :status_entered
WHERE employee_id = :employee_id_entered;


-- ORDERS TABLE

--returns all the orders from the past year
SELECT *
FROM Orders
where order_date >= CURDATE() - INTERVAL 365 DAY;


-- put an order into the system
INSERT INTO Orders (
    customer_id,
    employee_id,
    order_date,
    status,
    total_amount
)
VALUES (
    :value_for_customer_id,
    :value_for_employee_id,
    :value_for_order_date,
    :order_status,
    :calculated_full_amount
);

-- delete order from the system
DELETE FROM Orders
WHERE order_id = :order_id_selected_from_order_page;

-- update order status
UPDATE Orders 
SET status = :statusinput
WHERE order_id = :order_id_selected_from_order_page;


-- MENU ITEMS TABLE

-- select all menu items currently available
SELECT *
FROM MenuItems
WHERE current = 1;

-- insert a new menu item
INSERT INTO MenuItems (
    dish_name,
    price,
    description,
    category,
    current
)
VALUES (
    :dish_name_inserted,
    :price_inserted,
    :description_inserted,
    :categoy_inserted,
    :current_status_inserted
);


-- remove a menu item
DELETE FROM MenuItems
WHERE item_id = :item_id_chosen_on_menu_item_page;

-- update the price of a menu item
UPDATE MenuItems
SET price = :price_input,
WHERE item_id = :item_id_chosen_on_menu_item_page;



--ORDER DETAILS TABLE

--select all the details for a specific order_id
SELECT *
FROM OrderDetails
WHERE order_id = :order_id_selected_from_order_details_page;


-- add new order details
INSERT INTO OrderDetails (order_id, item_id, quantity, price)
SELECT
    o.order_id, 
    m.item_id, 
    :quantity_entered_from_order_details_page,
    m.price
FROM 
    Orders o
JOIN 
    MenuItems m ON m.dish_name = :dish_name_input
JOIN
    Customers c ON c.customer_id = o.customer_id
WHERE 
    c.customer_name = :customer_name_input AND 
    o.order_date = :order_date_input;



-- Update the quantity in the OrderDetails table
UPDATE OrderDetails
SET quantity = :quantity_entered
WHERE order_id = :order_id_entered;


-- Delete from order details based on order detail id
DELETE FROM OrderDetails
WHERE order_detail_id = :order_detail_id_input;
