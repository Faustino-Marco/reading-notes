# Reading Notes 02

## HTML

### Ch. 2: "Text" (p40-61)

- Tags (markup) used to add content to the page

#### Structural Markup
- elements used to describe both headings and paragraphs
- Headings
  - h1, h2, h3, h4, h5, h6
    - descending order of size
- Paragraphs
  - `<p>` tags used to open and close areas where text should start and finish


#### Semantic Markup
- provides extra info
  - where emphasis is placed in a sentence 
  ```html
  <em>italicized or emphasized text</em>
  ```

### Ch. 10: "Introducing CSS" (p226-245)

#### Thinking inside the box
- Block
  - look like they start on a new line
- inline
  - flow within the text
  - do not start on new line 
  ```html
  <b>, <i>, <img>, <em>, <span>
  ```
- Styling the way each individual box and its contents is presented

#### CSS & HTML

- css associates style elements with in html with its style rules

```css
p {
  font-family: Arial;
}

h1, h2, h3 {
  font-family: Arial;
  color: yellow;
}
```
- Format-- properties:values

#### INTERNAL CSS

- CSS can be written inline in the HTML document too
  - place style rules inside a `<style>` element
  - should use the type attribute to indicate styles are specified in CSS

  ```html
  <style type="text/css">
    body {
      font-family: arial;
      background-color: rgb(yadayadayada);
    }
    h1 {
      color: black;
    }
  ```

#### CSS SELECTORS
- allow you to target rules to diff elements in an html document
- case sensitive
  - must match element names and values EXACTLY
- universal: `*`
- type selector: matches element names `h1, h2 {}`
- class selector: `.note {}`
- id selector: `#`
- child selector `li> a {}`
  - targets any `a` elements that are children of an `<li>` element but no other a's
- descendant selector: `p a {}`
  - targets a elements within p element, even if there are other elements between them
- adjacent sibling: `h1+p {}`
  - targets first p element after any h1 elements, but no other p elements
- general sibling: `h1~p {}`
  - applies to any p elements that are sibs of h1, not just first p after h1

#### Cascading effect
- last rule
  - latter of two identical selectors takes precedence
- more specific selector takes precedence over more general ones
- you can add `!important` after any property to make it more important than other rules
```html
<h1>Potatoes</h1>
<p id="intro">There are <i>dozens</i> of different
<b>potato</b> varieties.</p>
<p>They are usually described as early, second early
 and maincrop potatoes.</p>
```
```css
* {
font-family: Arial, Verdana, sans-serif;}
h1 {
font-family: "Courier New", monospace;}
i {
color: green;}
i {
color: red;}
b {
color: pink;}
p b {
color: blue !important;}
p b {
color: violet;}
p#intro {
font-size: 100%;}
p {
font-size: 75%;}
```

#### Inheritance

- the value of any property will be inherited by child-elements

```
Before launching any new site,
it is important to test it in more
than one browser, because there
can be slight differences in how
browsers display the pages.
You do not need lots of
computers to test your site, as
there are online tools to show
you what a page looks like in
multiple browsers:
BrowserCam.com
BrowserLab.Adobe.com
BrowserShots.org
CrossBrowserTesting.com
```
```
Using these tools, it is a good
idea to check the site on
different operating systems (PC,
Mac, and Linux) and in older
versions of the major browsers,
as well as recent versions.
When you look at your site in
more than one browser, you
might find that some elements
on your page do not look as you
expect them to.
When a CSS property does
not display as expected, it
is generally referred to as a
browser quirk or CSS bug. 
```
```
Some common browser bugs are
discussed in this book, but there
are many smaller bugs that only
occur in rare situations, or on old
browsers that few people use.
If you come across a CSS bug,
you can use your favorite search
engine to try and find a solution.
Or you can check these sites:
PositionIsEverything.net
QuirksMode.org
```
## JS

### Ch. 2: "Basic JavaScript Instructions" (p53-84)
- uses series of instructions
  - each individual step is called a statement
- curly brackets start "code block"
- use comments to explain code (multi-line /* */)
- must be VERY specific

#### Variables
- variable keyword (var, const, let), variable name, assignment operator, value
- numeric, string, boolean
- variables store info
- escape with \ inside strings

- Rules
  - name must start with letter, $, or _, NOT A NUMBER
  - no dash - or period .
  - no keywords or reserved words are eligible for variable names (let, var, push, etc)
  - case sensitive
  - semantic 
  - camelCase

- Arrays
  - store multiple data values
  - index starts at 0
  - access with `name[i]`
- Expressions
  - assign a value to variable `var color = 'beige';` 
  - use two + values to return single value `var area = 3*2`
- Operators
  - ==, ===, !=, etc
  - increment, decrement, modulus
    - ++, --, %
  
### Ch. 4: "Decisions and Loops" (p145-162)
- Evaluations
  - analyze values in scripts

- Decisions
  - use results of evaluations to decide which path your script should take

- loops
  - perform same set of steps repeatedly

- conditions & conditional statements
  - if (condition) {
    code block
  }
  
- comparison ops
  - !=, <=, >, etc
- can be expressions enclosed in (parenthesis) < (this)

- logical ops
  - &&, ||, !,
- 