let form = document.querySelector("#signupForm");

form.addEventListener("submit", function(event){

    event.preventDefault(); 

    let name = document.querySelector("#name").value.trim();
    let email = document.querySelector("#email").value.trim();
    let phone = document.querySelector("#phone").value.trim();
    let password = document.querySelector("#password").value;
    let confirmPassword = document.querySelector("#confirmPassword").value;
    let terms = document.querySelector("#terms").checked;

    let nameError = document.querySelector("#nameError");
    let emailError = document.querySelector("#emailError");
    let phoneError = document.querySelector("#phoneError");
    let passwordError = document.querySelector("#passwordError");
    let confirmError = document.querySelector("#confirmError");
    let termsError = document.querySelector("#termsError");

    nameError.innerText = "";
    emailError.innerText = "";
    phoneError.innerText = "";
    passwordError.innerText = "";
    confirmError.innerText = "";
    termsError.innerText = "";

    let isValid = true;

    if(name === ""){
        nameError.innerText = "Name is required";
        isValid = false;
    }

    let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$/;

    if(!emailPattern.test(email)){
        emailError.innerText = "Enter a valid email";
        isValid = false;
    }

    let phonePattern = /^[0-9]{10}$/;

    if(!phonePattern.test(phone)){
        phoneError.innerText = "Phone must be 10 digits";
        isValid = false;
    }

    let passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    
    if(!passwordPattern.test(password)){
        passwordError.innerText = "Password must contain 1 uppercase, 1 lowercase, 1 number, 1 special character and be at least 8 characters long";
    }

    if(password !== confirmPassword){
        confirmError.innerText = "Passwords do not match";
        isValid = false;
    }

    if(!terms){
        termsError.innerText = "You must accept the terms";
        isValid = false;
    }

    if(isValid){
        alert("Registration Successful!");
        form.reset();
    }

});