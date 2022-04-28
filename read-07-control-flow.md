# Reading 007

## Control Flow

- *Control flow* is the order in which the computer executes statements in a script.
- Code is run in order from first line to last line
    - ***Unless*** the computer runs across the (extremely frequent) structures that change the control flow
        - conditionals
            - if/else
        - loops
- When you read a script, not only read start to finish, also look at program structure and how it affects order of execution.

## JS Functions 

- A JS function is a block of code designed to perform a particular task.
    - executed when "something" invokes it (calls it).
```
function myFunction(p1, p2) {
  return p1 * p2;   // The function returns the product of p1 and p2
}
```
### Function Syntax
- `function` keyword, followed by a **name**, followed by parentheses **()**.
- JS function names can contain letters, digits, underscores, and dollar signs (same as variables).
- parentheses may include parameter names separated by commas:
```
function name(parameter1, parameter2, parameter3) {
  // code to be executed
}
```
- function parameters: listed inside () in function def
- function arguments: values received by function when invoked
-   **Function is similar to Procedure or Subroutine in other programming languages.**
- Function calls
    - event occurs (user clicks a button)
    - invoked (called) from JS code
    - automatically (self invoked)
- Function Return
    - When JS reaches a `return` statement, the function will stop executing.
    - if invoked from statement, js will "return" to execute the code after the invoking statement.
    - Functions often compute a return value.
        - return value is "returned" back to the "caller".
```
let x = myFunction(4, 3);   
// Function is called, return value will end up in x

function myFunction(a, b) {
  return a * b;             
  // Function returns the product of a and b
}
```
### Why Functions
- Can be re-used after defining
```
function toCelsius(fahrenheit) {
  return (5/9) * (fahrenheit-32);
}
document.getElementById("demo").innerHTML = toCelsius(77);
```
    - `toCelsius` refers to the function object
    - `toCelcius()` refers to the function result
        - **Accessing a function without `()` will return the function object *instead of* the function result**.

### Functions as Variable Values
As opposed to using a variable substitute for a function's return value...
```
let x = toCelsius(77);
let text = "The temperature is " + x + " Celsius";
```

...You can simply use the function directly.
```
let text = "The temperature is " + toCelsius(77) + " Celsius";
```

### Local Variables

- Variables declared within a JS function become **LOCAL** to the function.
    - that means they can't be referenced outside the function
```
// code here can NOT use carName

function myFunction() {
  let carName = "Volvo";
  // code here CAN use carName
}

// code here can NOT use carName
```

## Operators

[site](https://www.w3schools.com/js/js_operators.asp)

- Assignment operator
    - `=`
        - x = 10
- `+` addition
- `-` subtraction
- `*` multiplication
- `**` exponentiation
- `/` division
- `%` modulus (division remainder)
- `++` increment
- `--` decrement