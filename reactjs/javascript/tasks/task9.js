async function getUsers(){
    let response = await fetch("https://jsonplaceholder.typicode.com/users");
    let users = await response.json();
    let list = document.getElementById("userList");
    users.forEach(function(user){
        let li = document.createElement("li");
        li.innerText = user.name;
        list.appendChild(li);

    })
}