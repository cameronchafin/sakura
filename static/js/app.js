// ----- Customers ----- //

// Delete customer
function setupDeleteCustomer(customerId) {
    document.getElementById('delete-customer-id').value = customerId;
}

// Update customer
function setupEdit(button) {
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


// ----- Menu Items ----- //
// Delete menu item
function setupDeleteMenuItem(itemId) {
    document.getElementById('delete-menu-item-id').value = itemId;
}



// ----- Orders ----- //




// ----- Order Details ----- //