const API = "http://127.0.0.1:8000";

let fiboBtn = document.getElementById("fiboBtn");
let factBtn = document.getElementById("factBtn");
let oddEvenBtn = document.getElementById("oddEvenBtn");
let armBtn = document.getElementById("armBtn");
let primeBtn = document.getElementById("primeBtn");

let popup = document.getElementById("popup");
let popupTitle = document.getElementById("popupTitle");
let popupInput = document.getElementById("popupInput");
let calcBtn = document.getElementById("calcBtn");
let popupResult = document.getElementById("popupResult");
let closeBtn = document.getElementById("closeBtn");

let slidePanel = document.getElementById("slidePanel");
let closeSlide = document.getElementById("closeSlide");
let startNum = document.getElementById("startNum");
let endNum = document.getElementById("endNum");
let primeCalcBtn = document.getElementById("primeCalcBtn");
let primeResult = document.getElementById("primeResult");

let currentOperation = "";

function openPopup(title, operation){
    popup.style.display = "flex";
    popupTitle.innerHTML = title;
    popupInput.value = "";
    popupResult.innerHTML = "";
    currentOperation = operation;
}

fiboBtn.addEventListener("click", () =>
    openPopup("Fibonacci Series", "fibonacci")
)

factBtn.addEventListener("click", () =>
    openPopup("Factorial of the number", "factorial")
)

oddEvenBtn.addEventListener("click", () =>
    openPopup("Odd or Even Number", "odd_even")
)

armBtn.addEventListener("click", () =>
    openPopup("Armstrong Number", "armstrong")
)

calcBtn.addEventListener("click", async function(){
    let num = Number(popupInput.value);
    let response = await fetch(API + "/" + currentOperation,{
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            number: num
        })
    })
    let data = await response.json();

    if(Array.isArray(data.result)){
        popupResult.innerHTML = data.result.join(", ");
    }
    else{
        popupResult.innerHTML = data.result;
    }

})

closeBtn.addEventListener("click", function(){
    popup.style.display = "none";
})

primeBtn.addEventListener("click", function(){
    slidePanel.classList.add("open");
    startNum.value = "";
    endNum.value = "";
    primeResult.innerHTML = "";
})

closeSlide.addEventListener("click", function(){
    slidePanel.classList.remove("open");
})

primeCalcBtn.addEventListener("click", async function(){
    let num1 = Number(startNum.value);
    let num2 = Number(endNum.value);

    let response = await fetch(API + "/prime_series", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            start: num1,
            end: num2
        })
    })
    let data = await response.json();
    primeResult.innerHTML = data.result.join(", ");
    
})