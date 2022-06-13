# READ 06: PROBLEM DOMAIN, OBJECTS, AND THE DOM

## JS

## OBJECT LITERALS

- ### Object
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

  - BASICS
    - access the elements
    - work with those elements
  
  - DOM Queries
    - `let itemOne getElementById('one);`
    - `querySelector('css selector');`
    - `getElementByClassName('class');`
    - `getElementByTagName('tagName');`
    - `querySelectorAll('css selector');`
    - can also get multiple elements that use one tag
  ```js
  var elements = document.getElementsByClassName('hot')
  if (elements.length>= 1) {
  var firstltem = elements.item(O);
  }
  ```
  - use a loop to get all elements in nodelist
  - can access, update, and change nodes with new nodevalues

