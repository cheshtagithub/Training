let count = 0;

let display = document.getElementById("count");

function updateColor(){

    if(count > 0){
        display.style.color = "green";
    }
    else if(count < 0){
        display.style.color = "red";
    }
    else{
        display.style.color = "black";
    }

}

function increase(){

    count++;

    display.innerText = count;

    updateColor();

}

function decrease(){

    count--;

    display.innerText = count;

    updateColor();

}

function resetCounter(){

    count = 0;

    display.innerText = count;

    updateColor();

}