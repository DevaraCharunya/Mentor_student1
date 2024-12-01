// JavaScript for interactivity

// Show the alert message when a link is clicked
function showAlert() {
    alert("You are about to view the details!");
}

// Optional: To show a custom alert message that can be styled
function showCustomAlert(message) {
    // Create the alert box element
    var alertBox = document.createElement('div');
    alertBox.className = 'alert';
    alertBox.innerText = message;
    
    // Append the alert box to the body
    document.body.appendChild(alertBox);

    // Display the alert and remove it after a few seconds
    setTimeout(function() {
        alertBox.classList.add('show');
    }, 100);

    setTimeout(function() {
        alertBox.classList.remove('show');
        setTimeout(function() {
            document.body.removeChild(alertBox);
        }, 300);
    }, 3000);
}
