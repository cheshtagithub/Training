// a = 12;
// b = '12';
// console.log(a==b);
// console.log(a===b);

// let fname = "Cheshta";
// let age = 21
// without template literal
// console.log("Hello my name is " + fname+" and i am "+age+" years old.");

// with template literal
// console.log(`Hello ${fname} and i am ${age} years old`);


// for(let i=1;i<=10;i++){
//     setTimeout(function(){
//         console.log(i);       
//     },i*1000)
// }

// function greet(name, callback){
//     console.log("Hello " + name);
//     callback();
// }

// function sayBye(){
//     console.log("Goodbye!");
// }

// greet("Cheshta", sayBye);

// let numbers = [1,2,3,4];

// let result = numbers.map(function(num){
//     return num * 2;
// });

// console.log(result);
let numbers = [1,2,3];

let result = numbers.map(n => n * 3);

console.log(result);