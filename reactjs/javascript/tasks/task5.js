// let a = document.querySelector("h1");
// console.log(a);

// a.innerText = "Welcome";
// console.log(a);


// a.innerHTML = "hihihihihi";
// console.log(a);

// a.style.color = "purple"
// a.style.backgroundColor = "black";

// let flag = 0;

// let bulb = document.querySelector("#bulb");
// let btn = document.querySelector("button");

// btn.addEventListener("click", function(){
//     if(flag == 0){
//         bulb.style.backgroundColor = "yellow";
//         flag = 1;
//     }
//     else{
//         bulb.style.backgroundColor = "transparent";
//         flag = 0;
//     }
// })

// let h = document.querySelector("h1");
// let btn = document.querySelector("button");
// let b = document.querySelector("body");
// let para = document.querySelector("p");
// let list = document.querySelector("ul")
// btn.addEventListener("click", function(){
//     let new_item = document.createElement("li");
//     new_item.textContent = "orange";
//     list.appendChild(new_item)
// })

let input = document.querySelector("#taskInput");
let button = document.querySelector("#addBtn");
let list = document.querySelector("#taskList");

button.addEventListener("click", function () {

    let taskText = input.value;

    let newTask = document.createElement("li");

    newTask.textContent = taskText;

    list.appendChild(newTask);

    input.value = "";


    newTask.addEventListener("click", function(){
        newTask.remove();
});

});

