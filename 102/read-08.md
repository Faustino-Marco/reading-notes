# Read 08 Operators and Loops

## Expressions and Operators
[link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators) 

### Assignment Operators
- simple assignment operator is equal `=`
    - x = f()
- addition assignment `+=`
    - x = x + f()
- subraction assignment `-=`
    - x = x - f()
- multiplication `*=`
- divsion `/=`
- remainder assignment `%=`
    - x = x % f()
- exponentiation `**=`
- ...etc...

### Comparison Operators

> A comparison operator compares its operands and returns a logical value based on whether the comparison is true. The operands can be numerical, string, logical, or object values. Strings are compared based on standard lexicographical ordering, using Unicode values. In most cases, if the two operands are not of the same type, JavaScript attempts to convert them to an appropriate type for the comparison. This behavior generally results in comparing the operands numerically. The sole exceptions to type conversion within comparisons involve the === and !== operators, which perform strict equality and inequality comparisons. These operators do not attempt to convert the operands to compatible types before checking equality. The following table describes the comparison operators in terms of this sample code: 

```
var var1 = 3;
var var2 = 4;
``` 

- Equal `==`
    - returns `true` if operands are equal
        - 3 == var1
        - "3" == var1
        - 3 == '3'
- Not equal `!=`
    - returns `true` if operands are not equal
        - var1 != 4
        - var2 != "3"
- Strict equal `===`
    - returns `true` if operands are equal AND of the same type
        - 3 === var1
- strict not equal `!==`
    - returns `true` if operands are of the same type but not equal, or are of different type
        - var1 !== "3"
        - 3 !== "3"
- `>`, `>=`, `<`, `<=`, also valid 



## Loops

[Text](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)

### For loops

```
for (let step = 0; step < 5; step++) {
  // Runs 5 times, with values of step 0 through 4.
  console.log('Walking east one step');
}
```

initialization  condition  update/increment
```
for ([initialExpression]; [conditionExpression]; [incrementExpression])
  statement
  ```

For example
```
for (let i = 0; i<= 12; i += 1) {
    console.log(i * 8);
}
```

### While loops

```
while (condition){
    statement
}
```
statement will execute until condition becomes false

`break` can be used to break out of loop


### Lecture Notes

while loops
    - run until condition is no longer met
for loops
    - run for a certain number of times


initialization  condition  update/increment
```
for ([initialExpression]; [conditionExpression]; [incrementExpression])
  statement
  ```

For example
```
for (let i = 0; i<= 12; i += 1) {
    console.log(i * 8);
}
```


#### truth table

using comparison operators can be used in loops, don't forget about || and &&
(OR and AND)