# Sakura Lounge 

## Description

Sakura Lounge is a popular sushi restaurant serving approximately 40,000 meals per year, pulling an annual revenue of $3 million. With a diverse sushi menu, from traditional sashimi to unique fusion rolls, the restaurant offers more than 100 different menu items.

This database management system is designed to manage and record a high volume of customer orders, detailed menu item data, and employee transactions. By tracking customer dining habits, popular dishes, and server performance, the database allows the restaurant management to refine their menu, optimize staff schedules, and enhance overall customer service and revenue.

This Flask-based web application It includes features for managing customers, employees, menu items, orders, and order details. The application uses a MySQL database to store and retrieve data.

## Table of Contents

- [Features](#features)
- [Dependencies](#dependencies)
- [Citation](#citation)

## Features

- Manage customers: Add, edit, and view customers.
- Manage employees: Add, edit, and view employees.
- Manage menu items: Add, edit, and view menu items.
- Manage orders: Add, edit, and view orders.
- Manage order details: Add, edit, and view order details.

## Dependencies

The project dependencies are listed in the `requirements.txt` file. Key dependencies include:

- Flask
- Flask-MySQLdb
- gunicorn
- python-dotenv
- mysqlclient

## Citation

This project includes adapted code and concepts from the following sources:

### Application Setup and Database Configuration

- **Configuring app and connecting to database**
  - **Date**: 6/8/2024
  - **Description**: Adapted from OSU Flask Starter APP
  - **URL**: [OSU Flask Starter APP](https://github.com/osu-cs340-ecampus/flask-starter-app)
  - **Files**: `app.py`, `db_connector.py`

  ### HTML Templates

- **Bootstrap Components (Navbar, Footer, Table, Modal)**
  - **Date**: 6/8/2024
  - **Description**: Adapted from Bootstrap documentation
  - **URL**: [Bootstrap Documentation](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
  - **Files**: `templates/base.html`, `templates/customers.html`, `templates/employees.html`, `templates/menu.html`, `templates/orders.html`, `templates/order_details.html`
