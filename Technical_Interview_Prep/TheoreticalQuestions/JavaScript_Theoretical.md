1. What is the difference between let, var, const?
let, var, and const are all used to declare a variable in js.

VAR
 - when you declare a variable using var, the scope of the variable will be global or function/locally scoped.
 - scope is global when a var variable is declared OUTSIDE a function
 - scope is local(private) when a var variable is declared INSIDE a function
 - var variables can be re-declared and updated
 - var should not be used because of the fact that it can constantly be redeclared and updated. because it doesn't even warn you when you redeclare and update the var variable, one problem scenario is this: if you had a var variable declared before and declared a new variable with the same name unknowingly it will overwrite the previous value you had for it.
 - var declarations are hoisted to the top and initialized as undefined.

LET
 - this is the most preferred way for variable declaration
 - the scope of let is inside the block that it is used in {}
 - let can be updated but not redeclared
 - the 2 main reasons why let is better than var: 1. when you use let you don't have to worry about if you used a same variable name because a variable can only exist within its scope. 2. a variable cannot be declared more than once within a scope (var can which results in problems)
 - let declarations are hoisted to the top and is not initialized, so if you use a let variable before declaration you will get a Reference Error.

CONST
 - variables declared with const maintain constant values
 - similar to let, const is block scoped
 - const CANNOT be redeclared or updated
 - a const object CANNOT be updated however the properties of the object CAN
 - const declarations are hoisted to the top but are not initialized

Variables created without a declaration always have a global scope even if they are inside a function.

2. What is prototype in javascript?
All js objects inherit properties and methods from a prototype

3. What is a closure?
A closure is a function that has access to the parent scope even after the parent function has closed.

4. Explain the event loop in node.js?
The event loop allows node.js to perform non blocking I/O operations by offloading operations to the system kernel whenever possible.

5. What is the meaning of the keyword this in javascript?
The this keyword refers to the object that it belongs to.

6. What is node.js?
node.js is a js runtime environment, it helps execute js code outside a web browser

7. What is the difference between null and undefined?
In js undefined is a type while null is an object. Undefined means a variable is declared but no value has been assigned to it. null is an assignment value, you can assign null to a variable

8. Explain settimeout in javascript?
setTimeout() method delays the call of a function by a specified number of milliseconds. An example of where this would be useful is in a REST call. Sometimes a GET request would not be able to finish before the page loads so we can delay the time it takes for the page to load by using this method.

9. What is the difference between javascript and node.js?
JavaScript is a language and Node.js is a js runtime environment.

10. What is hoisting in javascript?
So usually javascript files are executed from left right, top to bottom.Hoisting is a mechanism where you can bypass this and variables and function declared are moved to the top of their scope before code execution. So they are run at the beginning of the file no matter where you place them.

11. Difference between promise and a callback?
A promise, promises that it will return a value some time in the future. Promises start doing the task you give it right as the promise is invoked.
Callbacks tell the executing function what to do when the asynchrounous task completes.