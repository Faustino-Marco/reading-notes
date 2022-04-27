# CSS Notes 

## Reading Notes 

### What is CSS? 
[Site](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/What_is_CSS)
- Cascading Style Sheet
- Controls how HTML elements look in the browser, presenting your markup using whatever design you like.
- can use with .svg, .xml

#### Syntax 

- Rule-based language
- define rules by specifying styles to apply to particular elements/groups on your webpage 
- selector id's html element to style
- curly brackets
- declarations in pairs {prop:value;}
    - property (color, font-size, etc.)
    - value (red, 5em, etc.)
- MUST USE SEMICOLON
SEE INDIVIDUAL PROPERTY PAGES ON MDN

#### CSS Modules
MDN has a number of modules to practice CSS

#### CSS specifications

- all web standars tech's (html, css, js, etc.) have "specs" published by standards org's (W3C, WHATWG, ECMA, or Khronos) which define how the tech's are supposed to behave.
- CSS is dev'd by a group within W3C called the **CSS Working Group**
-CSS specs are intended for devs to use and implement support for features in 'user agents' (browsers).

#### Browser Support Info

- implementation status varies across browsers
    - some user agents aren't reading CSS the same as others
- browser support status is shown on MDN CSS property page in a sectoin called 'Browser Compatability'

### How to Add CSS 
[Site](https://www.w3schools.com/css/css_howto.asp)
- 3 ways to insert CSS
    - External CSS 
        - change look of entire site by changing one file
        - defined with a `<link>` inside the `<head>` section of an HTML page
    - Internal CSS 
        - defined within the `<style>` element, inside the `<head>` section
    - Inline CSS 
        - apply a unique style for a single element

#### Cascading Order
- css is read in cascading order and the lowest style is applied

### CSS Color 
- written in english;
- use #00ff00;(hex value)
- rgb(0,0,255); (rgb value)

Tip: use a background color in tandem with a text color that makes the text easy to read

[Site](https://www.w3schools.com/cssref/pr_text_color.asp)

#### Syntax
 - color: **color**|initial|inherit;

### CSS Reference 

Use [this link](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) to access the CSS reference page.

### Myers Web Reset Stylesheet 

Unclear at the moment what "reset CSS" is.

Link [here](https://meyerweb.com/eric/tools/css/reset/)


## Lecture Notes

### Box Model

from inside -> out 
1. content
2. padding 
3. border 
4. margin