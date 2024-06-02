// ----- Customers ----- //

// Delete customer
function setupDeleteCustomer(customerId) {
    document.getElementById('delete-customer-id').value = customerId;
}

// Update customer
function setupEditCustomer(button) {
    // Retrieve data attributes from the button
    var customerId = button.getAttribute('data-id');
    var customerName = button.getAttribute('data-name');
    var customerPhone = button.getAttribute('data-phone');
    var customerEmail = button.getAttribute('data-email');
    
    // Set the values in the modal's form
    document.getElementById('customerId').value = customerId;
    document.getElementById('inputName_edit').value = customerName;
    document.getElementById('inputPhone_edit').value = customerPhone;
    document.getElementById('inputEmail_edit').value = customerEmail;
}


// ----- Employees ----- //

// Delete employee
function setupDeleteEmployee(employeeId) {
    document.getElementById('delete-employee-id').value = employeeId;
}

// Update employee
function setupEditEmployee(button) {
    // Retrieve data attributes from the button
    var employeeId = button.getAttribute('data-id');
    var employeeName = button.getAttribute('data-name');
    var employeePhone = button.getAttribute('data-phone');
    var employeeEmail = button.getAttribute('data-email');
    var employeeCurrent = button.getAttribute('data-current');
    
    // Set the values in the modal's form
    document.getElementById('employeeId').value = employeeId;
    document.getElementById('inputName_edit').value = employeeName;
    document.getElementById('inputPhone_edit').value = employeePhone;
    document.getElementById('inputEmail_edit').value = employeeEmail;
    document.getElementById('selectCurrent_edit').value = employeeCurrent;
}


// ----- Menu Items ----- //
// Delete menu item
function setupDeleteMenuItem(itemId) {
    document.getElementById('delete-menu-item-id').value = itemId;
}

// Update menu item
function setupEditMenuItem(button) {
    // Retrieve data attributes from the button
    var itemId = button.getAttribute('data-id');
    var itemName = button.getAttribute('data-dish-name');
    var itemPrice = button.getAttribute('data-price');
    var itemDescription = button.getAttribute('data-description');
    var itemCategory = button.getAttribute('data-category');
    var itemCurrent = button.getAttribute('data-current');
    
    // Set the values in the modal's form
    document.getElementById('menuItemId').value = itemId;
    document.getElementById('inputDishName_edit').value = itemName;
    document.getElementById('inputPrice_edit').value = itemPrice;
    document.getElementById('inputDescription_edit').value = itemDescription;
    document.getElementById('selectCategory_edit').value = itemCategory;
    document.getElementById('selectCurrent_edit').value = itemCurrent;
}


// ----- Orders ----- //
function setupDeleteOrder(orderId) {
    document.getElementById('delete-order-id').value = orderId;
}

// Update order
function setupEditOrder(button) {
    // Retrieve data attributes from the button
    var orderId = button.getAttribute('data-id');
    var customerName = button.getAttribute('data-customer-name');
    var employeeName = button.getAttribute('data-employee-name');
    var orderDate = button.getAttribute('data-date');
    var orderStatus = button.getAttribute('data-status');

    
    // Set the values in the modal's form
    document.getElementById('orderId').value = orderId;

        // Set the customer dropdown
    var customerSelect = document.getElementById('selectCustomer_edit');
    for (var i = 0; i < customerSelect.options.length; i++) {
        if (customerSelect.options[i].text === customerName) {
            customerSelect.options[i].selected = true;
            break;
        }
    }

    // Set the employee dropdown
    var employeeSelect = document.getElementById('selectEmployee_edit');
    for (var i = 0; i < employeeSelect.options.length; i++) {
        if (employeeSelect.options[i].text === employeeName) {
            employeeSelect.options[i].selected = true;
            break;
        }
    }

    document.getElementById('inputOrderDate_edit').value = orderDate;
    
    // Set the status dropdown
    var statusSelect = document.getElementById('selectStatus_edit');
    for (var i = 0; i < statusSelect.options.length; i++) {
        if (statusSelect.options[i].text === orderStatus) {
            statusSelect.options[i].selected = true;
            break;
        }
    }
}

// ----- Order Details ----- //
function setupDeleteOrderDetail(orderDetailId) {
    document.getElementById('delete-order-detail-id').value = orderDetailId;
}