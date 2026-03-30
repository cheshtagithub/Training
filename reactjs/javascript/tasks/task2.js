// odd and even from 1 to 20

for(let i = 1; i <= 20; i++){
    if(i % 2 === 0){
        console.log(i,"is even number");
    }
    else{
        console.log(i,"is odd number");
        
    }
}


// eligible to vote or not
let age = 22;

if(age>=18){
    console.log("Eligible to vote");
}
else{
    console.log("Not eligible to vote");
    
}


//check if number is positive,negative or zero
let num = 12;

if(num<0){
    console.log("Negative");
}
else if(num===0){
    console.log("Zero");
}
else{
    console.log("Positive");
    
}


//print number from 10 to 1
//for loop
for(let i = 10; i >= 1; i--){
    console.log(i);
    
}

//while loop
let a = 10;
while(a > 0){
    console.log(a);
    a -= 1;
    
}