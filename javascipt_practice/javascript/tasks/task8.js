function fakeAPI(){

    return new Promise(function(resolve, reject){

        setTimeout(function(){

            let success = true;

            if(success){
                resolve(["Cheshta", "Rahul", "Aman"]);
            }
            else{
                reject("API failed");
            }

        },2000);

    });

}

async function loadUsers(){

    let status = document.getElementById("status");
    let list = document.getElementById("userList");

    status.innerText = "Loading...";

    try{

        let users = await fakeAPI();

        status.innerText = "Users Loaded";

        list.innerHTML = "";

        users.forEach(function(user){

            let li = document.createElement("li");
            li.innerText = user;

            list.appendChild(li);

        });

    }

    catch(error){

        status.innerText = error;

    }

}