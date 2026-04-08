const display = document.getElementById("display");

const buttons = document.querySelectorAll(".btn");

const equals = document.getElementById("equals");

const clear = document.getElementById("clear");

buttons.forEach(function(button){
    button.addEventListener("click", function(){
        display.value += button.innerText;
    })
})

equals.addEventListener("click", function(){
    display.value = eval(display.value);
})

clear.addEventListener("click",function(){
    display.value = "";
})