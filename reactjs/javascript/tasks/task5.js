// let a = document.querySelector("h1");
// console.log(a);

// a.innerText = "Welcome";
// console.log(a);


// a.innerHTML = "hihihihihi";
// console.log(a);

// a.style.color = "purple"
// a.style.backgroundColor = "black";


let bulb = document.querySelector("#bulb");
let btn = document.querySelector("button");
btn.addEventListener("click", function(){
    bulb.style.backgroundColor = "yellow";
})
