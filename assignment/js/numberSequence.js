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
let currentOperation = "";
let slidePanel = document.getElementById("slidePanel");
let closeSlide = document.getElementById("closeSlide");
let startNum = document.getElementById("startNum");
let endNum = document.getElementById("endNum");
let primeCalcBtn = document.getElementById("primeCalcBtn");
let primeResult = document.getElementById("primeResult");

fiboBtn.addEventListener("click", function(){
    popup.style.display = "flex";
    popupTitle.innerHTML = "Fibonacci Series";
    currentOperation = "fibonacci";
})

factBtn.addEventListener("click", function(){
    popup.style.display = "flex";
    popupTitle.innerHTML = "Factorial of the number";
    currentOperation = "factorial";
})

oddEvenBtn.addEventListener("click", function(){
    popup.style.display = "flex";
    popupTitle.innerHTML = "Odd or Even Number";
    currentOperation = "oddEven";
})

armBtn.addEventListener("click", function(){
    popup.style.display = "flex";
    popupTitle.innerHTML = "Armstrong Number";
    currentOperation = "armstrong";
})

calcBtn.addEventListener("click", function(){
    let num = Number(popupInput.value);
    if(currentOperation === "fibonacci"){
        let a = 0;
        let b = 1;
        let series = "0, 1, ";

        for(let i = 2; i < num; i++){
            let c = a + b;
            series += c + ", ";
            a = b;
            b = c;
        }
        popupResult.innerHTML = series;
    }
    else if(currentOperation === "factorial"){
        let product = 1;
        for(let i = 1; i <= num; i++){
            product *= i;
        }
        popupResult.innerHTML = product;
    }
    else if(currentOperation === "oddEven"){
        if(num % 2 === 0){
            popupResult.innerHTML = num + " is Even";
        }
        else{
            popupResult.innerHTML = num + " is Odd";
        }
    }
    else if(currentOperation === "armstrong"){
        let str = popupInput.value;
        let length = str.length;
        let sum = 0;

        for(let i = 0; i < length; i++){
            sum += Math.pow(str[i], length);
        }
        if(sum == str){
            popupResult.innerHTML = str + " is Armstrong";
        }
        else{
            popupResult.innerHTML = str + " is not Armstrong";
        }
    }
})

closeBtn.addEventListener("click", function(){
    popup.style.display = "none";
    popupInput.value = "";
    popupResult.innerHTML = "";
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

primeCalcBtn.addEventListener("click", function(){

    let num1 = Number(startNum.value);
    let num2 = Number(endNum.value);

    let primes = "";

    for(let i = num1; i <= num2; i++){

        if(i < 2) continue;

        let isPrime = true;

        for(let j = 2; j <= Math.sqrt(i); j++){

            if(i % j === 0){
                isPrime = false;
                break;
            }

        }

        if(isPrime){
            primes += i + ", ";
        }

    }

    primeResult.innerHTML = primes;

});
// fiboBtn.addEventListener("click", function(){
//     let num = Number(prompt("Enter the number"));
//     let a = 0;
//     let b = 1;
//     let series = "0 1 ";

//     for(let i = 2; i < num; i++){
//         let c = a + b;
//         series += c + " ";
//         a = b;
//         b = c;
//     }
//     result.innerHTML = series;
// })

// factBtn.addEventListener("click", function(){
//     let num = Number(prompt("Enter the number"));
//     let product = 1;
//     for(let i = 1; i <= num; i++){
//         product = product * i;
//     }
//     result.innerHTML = product;
// })

// oddEvenBtn.addEventListener("click", function(){
//     let num = Number(prompt("Enter the number"));
//     if(num % 2 == 0){
//         result.innerHTML = num + " is Even Number";
//     }
//     else{
//         result.innerHTML = num + " is Odd Number";
//     }
// })

// armBtn.addEventListener("click", function(){
//     let num = prompt("Enter the number");
//     let length = num.length;
//     let sum = 0;
//     for(let i = 0; i < length; i++){
//         sum += Math.pow(num[i], length);
//     }
//     if(sum == num){
//         result.innerHTML = num + " is an armstrong number";
//     }
//     else{
//         result.innerHTML = num + " is not an armstrong number";
//     }
// })

// primeBtn.addEventListener("click", function(){
//     let num1 = Number(prompt("Enter the starting number"));
//     let num2 = Number(prompt("Enter the ending number"));
//     let primes = "";
//     for(let i = num1; i <= num2; i++){
//         if(i < 2) continue;
//         let isPrime = true;
//         for(let j = 2; j <= Math.sqrt(i); j++){
//             if(i % j === 0){
//                 isPrime = false;
//                 break;
//             }
//         }
//         if(isPrime){
//             primes += i + " ";
//         }
//     }
//     result.innerHTML = primes;
// })