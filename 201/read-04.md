# Read 04

## HTML LINKS

- `<a href="http://www.imdb.com">IMDB</a>`
  - link and text user clicks on
- `<a href="index.html">Home</a>`
```html
<a href="reviews.html">Reviews</a>
<a href="music/listings.html">Listings</a>
<a href="movies/dvd/reviews.html">
Reviews</a>
<a href="../index.html">Home</a>
<a href="../../index.html">Home</a>
```
  - same folder
  - child folder
  - grandchild folder
  - parent folder
  - grandparent folder

  - mailto:
    - `<a href="mailto:jon@example.org">Email Jon</a>`

  - open link in new window
    - `<a href="http://www.imdb.com" target="_blank">`
  - link to same page
  ```html
  <h1 id="top">Film-Making Terms</h1>
<a href="#arc_shot">Arc Shot</a><br />
<a href="#interlude">Interlude</a><br />
<a href="#prologue">Prologue</a><br /><br />
<h2 id="arc_shot">Arc Shot</h2>
<p>A shot in which the subject is photographed by an
 encircling or moving camera</p>
<h2 id="interlude">Interlude</h2>
<p>A brief, intervening film scene or sequence, not
 specifically tied to the plot, that appears
 within a film</p>
<h2 id="prologue">Prologue</h2>
<p>A speech, preface, introduction, or brief scene
 preceding the the main action or plot of a film;
 contrast to epilogue</p>
<p><a href="#top">Top</a></p>
  ```


## CSS Ch. 15 - Layout

- block level starts on new line
- inline element flows between surrounding text
- relative positioning
  - moves an element in relation to where it wold have been in normal flow
  ```css
  p.example {
  position: relative;
  top: 10px;
  left: 100px;}
  ```
- absolute position
```css
h1 {
position: fixed;
top: 0px;
left: 50px;
padding: 10px;
margin: 0px;
width: 100%;
background-color: #efefef;}
p.example {
margin-top: 100px;}
```
- z index (opacity of layered boxes)
```css
h1 {
position: fixed;
top: 0px;
left: 0px;
margin: 0px;
padding: 10px;
width: 100%;
background-color: #efefef;
z-index: 10;}
p {
position: relative;
top: 70px;
left: 70px;}
```

- floats
```css
blockquote {
 float: right;
 width: 275px;
 font-size: 130%;
 font-style: italic;
 font-family: Georgia, Times, serif;
 margin: 0px 0px 10px 10px;
 padding: 10px;
 border-top: 1px solid #665544;
 border-bottom: 1px solid #665544;}
 ```

-clearing floats
```css

body {
width: 750px;
font-family: Arial, Verdana, sans-serif;
color: #665544;}
p {
width: 230px;
float: left;
margin: 5px;
padding: 5px;
background-color: #efefef;}
.clear {
clear: left;}
```
- columns
```html
<h1>The Evolution of the Bicycle</h1>
<div class="column1of2">
<h3>The First Bicycle</h3>
<p>In 1817 Baron von Drais invented a walking
 machine that would help him get around the
 royal gardens faster: two same-size ...</p>
</div>
<div class="column2of2">
<h3>Bicycle Timeline</h3> ...
</div>
```

```css
.column1of2 {
float: left;
width: 620px;
margin: 10px;}
.column2of2 {
float: left;
width: 300px;
margin: 10px;}
```

## JS - FUNCTIONS, METHODS, OBJECTS

### Functions
  - keyword + name + block is function

  - call by name with ();
  - use outer () if declaring variable that returns function within
  - Scope
    - variables declared in function are not accessible outside of said function

### Object
  - variables become properties
  - functions become methods
  ```js
  var hotel = {
    name: 'Quay',
    rooms: 49,
    booked: 48,
    gym: true,
    roomTypes: ['twin', 'double', 'suite'],
    checkAvailability: function() {
      return this.rooms - this.booked;
    }
  }
  ```
  - constructor notation
  ```js
  let hotel = new Object(rooms, booked) {
    hotel.name = 'Quay';
    hotel.rooms = rooms;
    hotel.booked = booked;
    hotel.checkAvailability = function() {
      return this.rooms - this.booked;
    }
  }
  ```
  - update object 
    - `hotel.name = 'Monte Carlo'`
    - `hotel[name]= 'Monte Carlo'`
    ```
    var elName = document.getElementByid   ('hotelName');
    elName.textContent = hotel . name;
    ```
  
  - THIS
    - keyword
      - `this.name` refers back to object it's inside
  - arrays are objects
    - can be inside of each other
  -Browser Object Model
    - window
      - document (current page)
      - history (pages in hist)
      - location (url of current page)
      - navigator (info about browser)
      - screen (display)

  ### JS OBJECTS
  - string (for string values)
    - p.128
    ```js
    let saying = 'Home sweet home ';

    saying.length = 16
    saying.toUpperCase();
    saying.toLowerCase();
    saying.charAt(12) = 'o';
    saying.indexOf('ee') = 7;
    saying.lastIndexOf('e') = 14;
    saying.substring(8,14)  = 'et hom';
    saying.split(' ') = ['home', 'sweet', 'home', ''];
    saying.trim() = 'Home sweet home' (no space)
    saying.replace('me', 'w') = 'How sweet home ';
    ```
  - number (numeric values)
  - boolean (boolean values)
  - date (dates)
  - math (calculations)
  - regex (matching patterns within strings of text)

  ### THE DOM
  - properties
    - `document.title; document.lastModified; document.URL; document.domain;`
  - methods
    - `document.write(); 
    - document.getElementById(); 
    - document.querySelectorAll();
      - returns list of elements that match a css selector (parameter);
    - document.createElement(); 
    - document.createTextNode();




