# Read: 06 - Dynamic web pages with JavaScript 

## Lecture Notes

- Using class attribute vs id attribute --> class can be used multiple times vs id can only be used once

ID Attribute:
```
<section id="give-it-a-name"></section>

section{
    property: value;
    color: green;
}
```

In CSS

```
#give-it-a-name {
    property: value;
}
```

Vs. Class Attribute:

```
<section class="here-a-name"></section>
```
In CSS:
```
.here-a-name {
    property: value;
    color: red;
}

h1, p {
    color: purple
}
```

## Reading Notes

### Intro Page

[Link](https://developer.mozilla.org/en-US/docs/Web/JavaScript) to intro.

> JavaScript (JS) is a lightweight, interpreted, or just-in-time compiled programming language with first-class functions. While it is most well-known as the scripting language for Web pages, many non-browser environments also use it, such as Node.js, Apache CouchDB and Adobe Acrobat. JavaScript is a prototype-based, multi-paradigm, single-threaded, dynamic language, supporting object-oriented, imperative, and declarative (e.g. functional programming) styles. Read more about JavaScript.

### Input and Output in JS

[Link](https://code-maven.com/input-output-in-plain-javascript) to Input/Output Page

Input/Output code example:

```
<html>
<head>
  <title>Hello World</title>
</head>
<body>
 
First name: <input id="first_name">
Last name: <input id="last_name">
<button id="say">Say hi!</button>
 
<hr>
<div id="result"></div>
 
<script>
function say_hi() {
    var fname = document.getElementById('first_name').value;
    var lname = document.getElementById('last_name').value;
 
    var html = 'Hello <b>' + fname + '</b> ' + lname;
 
    document.getElementById('result').innerHTML = html;
}
 
document.getElementById('say').addEventListener('click', say_hi);
</script>
 
</body>
</html>
 ```

Above we can see that JS makes it possible to input name and output something like "hello + input", while using a click button.

This can be cumbersome in html and JS has a page of templates available to shortcut the process of typing out all of the input/output in html.

[Here](https://code-maven.com/introduction-to-handlebars-javascript-templating-system)'s the link to that template.

### Variables in JS

[Link](https://www.w3schools.com/js/js_variables.asp) to Variables article

#### Declaring Variables

- There are 4 ways we can declare variables in JS
    - var
    - let
    - const
    - nothing??

- What are Variables?
    - Variables are containers for storing data
```
var x = 5;
var y = 6; 
var z = x + y;
```
can also use `let` or `const`
```
let x = 5;
let y = 9;
let z = y - x;
```
or use undeclared variables
```
x = 4;
y = 2;
z = x * y;
```

> When to Use JavaScript var?
Always declare JavaScript variables with var,let, or const.
The var keyword is used in all JavaScript code from 1995 to 2015.
The let and const keywords were added to JavaScript in 2015.
If you want your code to run in older browser, you must use var.

Use const for unchanging Variables, let for changing variables. 

Eg:
```
const price1 = 5;
const price2 = 6;
let total = price1 + price2;
```

after declaring a variable with let or var, assign a value using `=`

text is called "string" and numbers are "int"

It's possible to declare multiple variables in one statement.

```
let person = "John Doe", carName = "Volvo", price = 200;
```
Or you can use multiple lines for one declaration:
```
let person = "John Doe",
carName = "Volvo",
price = 200;
```

#### Re-Declaring Values

You CAN re-declare values using var, but not let
```
var carName = "Volvo";
var carName;
```
carName will not lose its value here, but it would lose its value if you were to have used `let` instead of `var`.

#### JS Arithmetic

JS can do arithmetic such as:
```
let x = 5 + 2 + 3;
```
#### JS Dollar Sign $$$
The dollar sign is considered a letter in JS so the following are all valid variables
```
let $ = "Hello World";
let $$$ = 2;
let $myMoney = 5;
```

### Bookmark Video Page

In this reading assignment we were also given a link to a series of videos that briefly explain how computers work.

[Here](https://www.youtube.com/playlist?list=PLzdnOPI1iJNcsRwJhvksEo1tJqjIqWbN-)'s that site with the videos.