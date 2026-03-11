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
