# Class 01 Reading Notes

## HTML/CSS

### Structure
- html pages are documents
  - html uses tags
    - often referred to as elements
    - opening tags carry attributes
      - attributes require a name & value
- html describes the structure of pages
```html
<html>
  <body>
    <h1>This is the main heading</h1>
    <p>paragraph</p>
    <h2>this is a subheading</h2>
    <p>here's another paragraph</p>
    <h2>another subheading</h2>
    <p>and another paragraph</p>
  </body>
</html>
```
- elements
  - <p> these are basic element tags
- attributes tell us more about elements
```html
<p lang="en-us">Paragraph in English</p>
```

### Extra Markup

### HTML5 Layout
- body/head/title
### Process & Design

## JS

### ABC of Programming

#### A
- What is JS
- a script is a series of instructions your computer can follow to achieve a goal
1. Define the Goal
  - puzzle to solve
2. Design the Script
  - series of tasks (flowchart)
  - write down steps for computer for each task (recipe)
```
1. Find the height of the first person
2. Assume he or she is the "tallest person"
3. Look at the height of the remaining people oneby-one and compare their height to the "tallest
person" you have found so far
4. At each step, if you find someone whose height is
greater than the current "tallest person", he or she
becomes the new "tallest person"
5. Once you have checked all the people, tell me
which one is the tallest
```

3. Code Each Step
  - must be written in a coding language the computer understands
  - take time to design script
- B
  - how do computers fit in with world around them
  - objects and properties
  #### objects
    - things
    - different types
    - properties
      - describe or define object
    - events
      - like cpu sticking it's hand up to say "this just happened!"
      - often used to trigger functionality
    - methods
      - tell you something about that object
      - change the value of one or more of that object's properties
```
  event: accelerate
  method changeSpeed();
  properties: current speed: 45mph
  #### properties
    - characteristics
    - each have name and value
```
`document` object represents an html page
properties ie title
methods ie getting info or adding/changing content
events ie clicking

- Browser sees webpage
  - receives page as html code
  - creates a model of the page and stores it in memory
  - use a rendering engine to show the page on screen
- C
  - how do i write a script for a web page?
  - html, css, js
  - use objects and methods
    - `document.write('Good Afternoon!');`
      object, member operator, method, parameters