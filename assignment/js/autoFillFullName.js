const firstName = document.getElementById("fname");
const lastName = document.getElementById("lname");
const fullName = document.getElementById("fullName");

function updateFullName() {
    fullName.value = firstName.value + " " + lastName.value;
}

// Run function whenever user types
firstName.addEventListener("input", updateFullName);
lastName.addEventListener("input", updateFullName);