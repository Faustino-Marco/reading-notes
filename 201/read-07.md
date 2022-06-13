# READ 07: OOP & HTML TABLES

## DOMAIN MODELING
- process of creating a conceptual model in code for a specific problem
  - an entity that stores data in propert9es and encapsulates behaviors in methods is commonly reffered to as an object-oriented model
- properties, data, types
- epic fail example
```js
var EpicFailVideo = function(epicRating, hasAnimals) {
  this.epicRating = epicRating;
  this.hasAnimals = hasAnimals;
}

EpicFailVideo.prototype.generateRandom = function(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

var parkourFail = new EpicFailVideo(7, false);
var corgiFail = new EpicFailVideo(4, true);

console.log(parkourFail.generateRandom(1, 5));
console.log(corgiFail.generateRandom(1, 5));
```
- include functions in objects to accomplish calculations and other tasks

- great for modeling a single entity that'll have many instances
- model attributes with a constructor function that defines and initalizes properties
- model behaviors with small methods that focus on doing one job well 
- create instances using the `new` keyword followed b a call to a constructor function
- Store the newly created object in a variable so you can access its properties and methods from outside
- use the `this` variable within methods so you can access the object's properties and methods from inside

## HTML TABLES

- table represents information in a grid format
- examples of tables include financial reports, tv schedules, and sports results
- tags
  - `<table> <th> <tr> <td>`
  - colspan
    - can be used on a `<th>` or a `<td>` element
      - to stretch across more than one column
      - use colspan in tag
        - `<td colspan="2">Geography</td>`
      - use rowspan in tag for rows
  - longtables
    - `<thead>, <tbody>, <tfoot>`
- width and spacing
```html
<table width="400" cellpadding="10" cellspacing="5">
 <tr>
 <th width="150"></th>
 <th>Withdrawn</th>
 <th>Credit</th>
 <th width="150">Balance</th>
 </tr>
 <tr>
 <th>January</th>
 <td>250.00</td>
 <td>660.50</td>
 <td>410.50</td>
 </tr>
 <tr>
 <th>February</th>
 <td>135.55</td>
 <td>895.20</td>
 <td>1170.15</td>
 </tr>
</table>
```
- apply borders
```html
<table border="2" bgcolor="#efefef">
 <tr>
 <th width="150"></th>
 <th>Withdrawn</th>
 <th>Credit</th>
 <th width="150" bgcolor="#cccccc">Balance</th>
 </tr>
 <tr>
 <th>January</th>
 <td>250.00</td>
 <td>660.50</td>
 <td bgcolor="#cccccc">410.50</td>
 </tr>
 <tr>
 <th>February</th>
 <td>135.55</td>
 <td>895.20</td>
 <td bgcolor="#cccccc">1170.15</td>
 </tr>
</table>
```

## JS

- ch. 3 see [Read-04](201/read-04.md)






