// Create a function that:
// takes a name
// prints Hello <name>, welcome to JavaScript
function greet(name){
    console.log(`Hello ${name}, Welcome to JavaScript`);    
}
greet("Rahul");


// Create a function that:
// takes a number
// returns the square
function square(num){
    return num*num;
}
let result = square(66);
console.log(result);


// Create a function that:
// takes a number
// returns "Even" or "Odd"
function checkNumber(num1){
    if(num1 % 2 == 0){
        console.log("Even");
    }
    else{
        console.log("odd");        
    }
}
checkNumber(9090909);


//Create a function that:
// takes two numbers
// returns the larger number
function maxNumber(a, b){
    if(a > b){
        console.log(a);        
    }
    else if(b > a){
        console.log(b);        
    }
    else{
        console.log("Both are equal");
    }
}
maxNumber(8787, 9856);


// Create a function that:
// takes three subject marks
// returns the total
function totalMarks(a, b, c){
    return a + b + c;
}
let total = totalMarks(99, 56, 89);
console.log(total);


//  Using arrow function, function expresion

// Create an arrow function that prints: Hello <name>
let greet = (name) => `Hello ${name}`;
console.log(greet("Rahul"));



// Create an arrow function that returns the cube of a number.
let cube = num => num**3;
console.log(cube(4));



// Largest Number (3 numbers)
let max = (a, b, c) => {
    if(a >= b && a >= c){
        return a;
    }
    else if(b >= a && b >= c){
        return b;
    }
    else{
        return c;
    }
};

console.log(max(5,10,7));



// Celsius to Fahrenheit
let convert = c => (c * 9/5) + 32;

console.log(convert(30));