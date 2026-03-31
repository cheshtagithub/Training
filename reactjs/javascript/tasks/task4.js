let fruits = ["apple", "banana", "mango", "orange"];
console.log(fruits[1], fruits[3]);


let num = [10,20,30];
num.push(40);
console.log(num);


let n = [5,10,15,20,25];
n.forEach(nums => {
    console.log(nums);
});

let number = [2,4,6,8];
let triple = number.map(num => num * 3);
console.log(triple);


let a = [11,18,25,30,42];
let num1 = a.filter(num => num > 20);
console.log(num1);


let info = [
    {name: "Rahul", age: 21, city: "Delhi"}
]
console.log(info[0].name,info[0].city);


let product = [
    {
        name: "Laptop",
        price: 60000
    }
];
product[0].price = 65000
console.log(product);

let student = {
 name: "Amit",
 marks: 85
};
student.grade = "A";
console.log(student);


let car = {
 brand: "Toyota",
 model: "Fortuner",
 year: 2022
}
for(let key in car){
    console.log(key, car[key]);
    
}

let users_info = [
 {id:1,name:"Rahul",age:22},
 {id:2,name:"Priya",age:19},
 {id:3,name:"Amit",age:25}
]
users_info.forEach(user => {
    console.log(user.name);   
}
)




let users = [
    {id:1, name:"Rahul", age:22},
    {id:2, name:"Priya", age:19},
    {id:3, name:"Amit", age:25}
];


//  Display all users
console.log("All Users:");
users.forEach(user => {
    console.log(user.id, user.name, user.age);
});


//  Add a new user
users.push({id:4, name:"Neha", age:23});

console.log("After Adding User:");
console.log(users);


//  Update user age
users.forEach(user => {
    if(user.id === 2){
        user.age = 20;
    }
});

console.log("After Updating Priya's age:");
console.log(users);


// Delete a user
let filteredUsers = users.filter(user => user.id !== 1);

console.log("After Removing Rahul:");
console.log(filteredUsers);