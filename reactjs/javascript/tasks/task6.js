// Button Click Action

let button = document.getElementById("clickBtn");
let message = document.getElementById("message");

button.addEventListener("click", function(){

    message.textContent = "Button was clicked successfully!";

});



// Form Validation

let form = document.getElementById("myForm");
let nameInput = document.getElementById("name");
let emailInput = document.getElementById("email");
let error = document.getElementById("error");

form.addEventListener("submit", function(event){

    if(nameInput.value.trim() === "" || emailInput.value.trim() === ""){
        
        event.preventDefault();
        error.textContent = "Please fill all fields.";

    }
    else{
        error.textContent = "Form submitted successfully!";
    }

});