-- This file features the data definition queries from which the database
-- server used to host this application's database is sourced

SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

DROP TABLE IF EXISTS Customers;
CREATE TABLE Customers (
    customer_id int(11) NOT NULL AUTO_INCREMENT,
    customer_name varchar(255) NOT NULL,
    phone_number varchar(100) NOT NULL,
    email varchar(255) NOT NULL,
    PRIMARY KEY(customer_id)
);

DROP TABLE IF EXISTS MenuItems;
CREATE TABLE MenuItems(
    item_id int(11) NOT NULL AUTO_INCREMENT,
    dish_name text NOT NULL,
    price decimal(10,2) NOT NULL,
    description text NULL,
    category ENUM('Nigiri', 'Sashimi', 'Maki Rolls', 'Specialty Rolls', 'Appetizers', 'Desserts', 'Beverages') NOT NULL,
    current boolean NOT NULL, -- 0 is false (not current) 1 is true (current)
    PRIMARY KEY(item_id)
);

DROP TABLE IF EXISTS Employees;
CREATE TABLE Employees (
    employee_id int(11) NOT NULL AUTO_INCREMENT,
    employee_name varchar(255) NOT NULL,
    phone_number varchar(100) NOT NULL,
    email varchar(255) NOT NULL,
    current boolean NOT NULL, -- 0 is false (not current) 1 is true (current)
    PRIMARY KEY(employee_id)
);

DROP TABLE IF EXISTS Orders;
CREATE TABLE Orders (
    order_id int(11) NOT NULL AUTO_INCREMENT,
    customer_id int NOT NULL,
    employee_id int,
    order_date datetime NOT NULL,
    status ENUM('Placed', 'Preparing', 'Served', 'Paid') NOT NULL, -- Placed, Preparing, Served, Paid
    total_amount decimal(10,2) NOT NULL,
    PRIMARY KEY(order_id),
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id) ON DELETE RESTRICT,  -- do not want to allow delete customer_id since customer could have multiple orders
    FOREIGN KEY(employee_id) REFERENCES Employees(employee_id) ON DELETE RESTRICT   -- do not want to allow delete employee_id since employee can be set to inactive if fire / quit
);

DROP TABLE IF EXISTS OrderDetails;
CREATE TABLE OrderDetails(
    order_detail_id int(11) NOT NULL AUTO_INCREMENT,
    item_id int(11) NOT NULL,
    order_id int(11) NOT NULL,
    quantity int(11) NOT NULL,
    price decimal(10,2) NOT NULL,
    PRIMARY KEY(order_detail_id),
    FOREIGN KEY(item_id) REFERENCES MenuItems(item_id) ON DELETE RESTRICT,
    FOREIGN KEY(order_id) REFERENCES Orders(order_id) ON DELETE RESTRICT
);

INSERT INTO Customers (
    customer_name,
    phone_number,
    email
)
VALUES (
    'John Doe',
    '213-485-6048',
    'jdoe@gmail.com'
),
(
    'Bob Smith',
    '213-445-6678',
    'bsmith@gmail.com'
),
(
    'Bob Joe',
    '213-908-3456',
    'bjoe@gmail.com'
),
(
    'Ricky Bobby',
    '213-333-4455',
    'rbobby@gmail.com'
),
(
    'Ned Flanders',
    '213-987-4456',
    'nflanders@gmail.com'
);

INSERT INTO MenuItems (
    dish_name,
    price,
    description,
    category,
    current
)
VALUES (
    'Salmon Nigiri',
    5.00,
    'Fresh salmon over a bed of seasoned rice',
    'Nigiri',
    1
),
(
    'Hamachi Sashimi',
    7.00,
    'Premium yellowtail, served with jalapeno slices',
    'Sashimi',
    1
),
(
    'Spicy Tuna Roll',
    6.00,
    'Tuna mixed with spicy mayo and scallions',
    'Maki Rolls',
    1
),
(
    'Takoyaki',
    5.00,
    'Octopus balls topped with mayo and bonito flakes',
    'Appetizers',
    1
),
(
    'Mochi',
    6.00,
    'Sweet rice cake filled with ice cream',
    'Desserts',
    1
);

INSERT INTO Employees(
    employee_name,
    phone_number,
    email,
    current
)
VALUES (
    'Teddy Bear',
    '213-422-3366',
    'tbear@gmail.com',
    1
),
(
    'Bill Nye',
    '213-896-3314',
    'bnye@gmail.com',
    1
),
(
    'Homer Simpson',
    '213-826-7864',
    'hsimpson@gmail.com',
    1
),
(
    'Peter Griffin',
    '213-284-4421',
    'pgriffin@gmail.com',
    0
),
(
    'Peter Parker',
    '213-563-7864',
    'pparker@gmail.com',
    1
);

INSERT INTO Orders(
    customer_id,
    employee_id,
    order_date,
    status,
    total_amount
)
VALUES (
    1,
    5,
    '2024-02-01',
    'Paid',
    20.00
),
(
    2,
    3,
    '2024-02-02',
    'Paid',
    27.00
),
(
    3,
    3,
    '2024-02-03',
    'Paid',
    28.00
);

INSERT INTO OrderDetails(
    item_id,
    order_id,
    quantity,
    price
)
VALUES (
    1,
    1,
    2,
    5.00
),
(
    4,
    1,
    2,
    5.00
),
(
    1,
    2,
    3,
    5.00
),   
(
    3,
    2,
    2,
    6.00
),
(
    2,
    3,
    4,
    7.00
);

SET FOREIGN_KEY_CHECKS=1;
COMMIT;