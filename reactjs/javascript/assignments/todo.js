const addBtn = document.getElementById("addBtn");
const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");

addBtn.addEventListener("click", function(){
    let taskText = taskInput.value;
    
    if(taskText === ""){
        alert("Enter a task");
        return;
    }

    let li = document.createElement("li");
    li.innerText = taskText;
    let deleteBtn = document.createElement("button");

    deleteBtn.innerText = "Delete";
    deleteBtn.classList.add("deleteBtn");
    deleteBtn.addEventListener("click", function(){
        li.remove();
    })
    li.appendChild(deleteBtn);
    taskList.appendChild(li);
    taskInput.value = "";
})