# Class 03 Lecture Notes

## JS Arrays

- A collection or a list of different

```js
'use strict';

let myArr = [1, 2, 3, 4, 5];

console.log(myArr);
console.table(myArr);
```

```js
'use strict';
let mixedArr = [1, 'hello', false, [1,2,3]];

console.table(mixedArr);
```

```js
'use strict';

let students = ['Kris', 'Matthew', 'Ricky', 'Elaine', 'Scottie'];

<!-- let matthew = students[1]

console.log(matthew);

let scottie = students.pop();
console.log(scottie);
console.log(students);
let poppedStudent = students.pop();
console.log(poppedStudent);
console.log(students); -->

students[10] = 'Stephanie';

console.log(students)

```

## CSS Box Modeling

- width/height
- padding
- border
- margin
- (position?)

```html
<header>
    <div>Div 1</div>
    <div>Div 2</div>
    <div>Div 3</div>
</header>
```

```css
div {
    border: solid-black;
    display: inline-block;
    margin: 5px;
}
header {
    border: solid red 5px;
    /* padding-top: 20px;
    padding-left: 15px; */
    padding: 20px, 20px, 15px;
    width: max-content;
    margin: 0 auto;
}
```

## JS Loops

### For Loops

```js

let students = ['Kris', 'Matthew', 'Ricky', 'Elaine', 'Scottie'];

for(let i = 0; i < students.length; i++){
  console.log(`Hello ${students[i]}!`);
}

for(let i = 0; i < students.length; i++){
  if(students[i] === 'Ricky'){
    console.log('Hey Ricky!');
  } else {
    console.log(`Get to work ${students[i]}`);
  }
}
```

### While Loops

- Anatomy
```js
while(condition){
    codeblock
}
```
```js

// let students = ['Kris', 'Matthew', 'Ricky', 'Elaine', 'Scottie'];

// for(let i = 0; i < students.length; i++){
//   console.log(`Hello ${students[i]}!`);
// }

// for(let i = 0; i < students.length; i++){
//   if(students[i] === 'Ricky'){
//     console.log('Hey Ricky!');
//   } else {
//     console.log(`Get to work ${students[i]}`);
//   }
// }
let myNumber = 30;

let userGuess = prompt('What number am I thinking of?');

while(userGuess != myNumber){
    userGuess = prompt('What number am I thinking of?');
}
```