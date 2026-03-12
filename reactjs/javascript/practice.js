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


for(let i=1;i<=10;i++){
    setTimeout(function(){
        console.log(i);       
    },i*1000)
}
