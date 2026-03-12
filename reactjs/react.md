### Javascript basics
#### var,const,let
1. var: Used to store data and can be changed. A variable declared with var works in the whole function, even if you write it inside a block.

2. const: Used to store data and cannot be changed.

3. let: Used to store data. A variable declared with let works only inside the block { } where it is created.

#### hoisting
var and functions are hoisted means there declaration is moved to the top.  
Example: 
```bash
console.log(a);
var a = 10;
this will give output : undefined
```

#### types in js
1. primitive: These store simple values.  
Example: number, string, boolean,etc.
2. Non-Primitive Types (Reference Types): These store collections of data.  
Example: object,array, function,etc.

```bash
In simple words, aisi koi bhi value jise copy krne par real copy nhi hota, balki us main value ka reference pass ho jata hai, use hm reference value kehte hai, or reference value ko direct copy nhi krte.or jis value ko copy krne pr real copy ho jaye vo primitive value hoti hai.
```

#### === in javascript
In javascript we do not have types like int, string, float,etc.
in js we only have let, var and const.
so if we want to compare 2 values in javascript a and b like follows:
```bash
a = 5;
b = '5';
console.log(a==b)
[Running] node "/home/cheshta/Desktop/Training/reactjs/javascript/practice.js"
true
```
the above code gives true in output even when a is number and b is string, this is because in javascript == only checks value, that's why we use === as it checks value as well ase type
```bash
a = 12;
b = '12';
console.log(a==b);
console.log(a===b);
[Running] node "/home/cheshta/Desktop/Training/reactjs/javascript/practice.js"
true
false
```
#### template literals
In JavaScript, Template Literals are a way to write strings using backticks ( ) instead of single (' ') or double (" ") quotes. They make string interpolation and multi-line strings easier.
```bash
let fname = "Cheshta";
let age = 21
// without template literal
console.log("Hello my name is " + fname+" and i am "+age+" years old.");

// with template literal
console.log(`Hello ${fname} and i am ${age} years old.`);
Output:
Hello my name is Cheshta and i am 21 years old.
Hello Cheshta and i am 21 years old.
```
#### setTimeout() in JavaScript
setTimeout() is used to execute a function after a specified delay (in milliseconds).

**Syntax**
```bash
setTimeout(function, delay, ...arguments)
```
```bash
for(let i=1;i<=10;i++){
    setTimeout(function(){
        console.log(i);       
    },i*1000)
}
Output:
[Running] node "/home/cheshta/Desktop/Training/reactjs/javascript/practice.js"
1
2
3
4
5
6
7
8
9
10
[Done] exited with code=0 in 10.269 seconds
```

# ReactJS
React is a powerful JavaScript library for building fast, scalable front-end applications. Created by Facebook, it's known for its component-based structure, single-page applications (SPAs), and virtual DOM,enabling efficient UI updates and a seamless user experience.

## Why Learn React?
Before React, front-end development struggled with:  
**Manual DOM Manipulation:** Traditional JavaScript directly modified the DOM, slowing down the performance.
**Complex State Management:** Maintaining UI state became messy and hard to debug.
**Tight Coupling in Frameworks:** Frameworks like Angular introduced complex two-way data binding that made code harder to manage.  
React solved these issues with a modern and modular approach.

## Make react program 
Run the following command in the terminal:  
```bash
cheshta@cheshta-Latitude-E7470:~/Desktop/Training/reactjs$ npm create vite@latest my-react-app
```
To run the code , run following command
```bash 
npm run dev
```
