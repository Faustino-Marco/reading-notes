# Read: 03 - HTML Lists, CSS Boxes, JS Control Flow

## HTML/CSS Ch. 3 - HTML Lists

### OL
- ordered lists
  - `<ol>` containing `<li>`'s
  - numbers
### UL
- unordered lists
  - `<ul>` containing `<li>`'s
  - bullets

### DL
- definition lists
  - `<dl>` consists of a series of terms and their definitions
    - contains `<dt>`'s and `<dd>`'s
    - term being defined
    - definition.
```html
<dl>
<dt>Sashimi</dt>
<dd>Sliced raw fish that is served with
 condiments such as shredded daikon radish or
 ginger root, wasabi and soy sauce</dd>
<dt>Scale</dt>
<dd>A device used to accurately measure the
 weight of ingredients</dd>
<dd>A technique by which the scales are removed
 from the skin of a fish</dd>
<dt>Scamorze</dt>
<dt>Scamorzo</dt>
<dd>An Italian cheese usually made from whole
 cow's milk (although it was traditionally made
 from buffalo milk)</dd>
</dl>
```

### Nested lists
- you can put a second list inside another list

## HTML/CSS ch. 13 - CSS Boxes

### Dimensions
- width, height
- background color
- % apply to parent element
  - `width: 90%;` (of parent's width)

- limiting width
  - `min-width: 450px;`
  -  `max-widt: 650px;`
- limiting height
  - same applies to height
    - this way paragraphs don't overlap
- overflow content
  - `overflow: hidden`
  - `overflow: scroll`

### BORDER, MARGIN, PADDING

- adding space between various items
- Border
```css
p.one {
border-width: 2px;}
p.two {
border-width: thick;}
p.three {
border-width: 1px 4px 12px 4px;}
```
- clockwise dimensions
  - border style
```css
p.one {border-style: solid;}
p.two {border-style: dotted;}
p.three {border-style: dashed;}
p.four {border-style: double;}
p.five {border-style: groove;}
p.six {border-style: ridge;}
p.seven {border-style: inset;}
p.eight {border-style: outset;}
```
  - border color
```css
p.one {
border-color: #0088dd;}
p.two {
border-color: #bbbbaa #111111 #ee3e80 #0088dd;}
```
  - shorthand border
```css
p {
width: 250px;
border: 3px dotted #0088dd;}
```
  - PADDING 
    - space between content of element and its border
```css
p {
width: 275px;
border: 2px solid #0088dd;}
p.example {
padding: 10px;}
```
    - can use clockwise notation too
  - MARGIN
```css
p {
width: 200px;
border: 2px solid #0088dd;
padding: 10px;}
p.example {
margin: 20px;}
``` 
```
Sometimes you might see the
following, which means that the
left and right margins should be
10 pixels and the top and bottom
margins should be 20 pixels:
margin: 10px 20px;
(This same shorthand shown
above can also be applied to
padding.)
```

- centering content
  - set left & right margin to auto
  -   child element should have   `text-align: left/right;`
  - ^ necessary if you want a child of a centered parent to be off-center
  - internet explorer 6 quirk
    - uses margin and padding in width
      - workaround with doctype (html5)
- change inline/block
  - display property has values that can turn an inline element into block or vise versa
    - inline
      - causes block-level to act like inline
    - block
      - causes inline element to act like block
    - inline-block
      - causes block-level element to flow like inline, while retaining other features of a block-level element
    - none
      - hides an element from the page
        - as though not on page at all
    - visibility
      - none or visible
    - border images
    ```
    1: The URL of the image
    2: Where to slice the image
    3: What to do with the straight
    edges; the possible values are:
    stretch stretches the image
    repeat repeats the image
    round like repeat but if the
    tiles do not fit exactly, scales
    the tile image so they will
    ```

    - box shadows
    ```css
    p.one {
    -moz-box-shadow: -5px -5px #777777;
    -webkit-box-shadow: -5px -5px #777777;
    box-shadow: -5px -5px #777777;}
    p.two {
    -moz-box-shadow: 5px 5px 5px #777777;
    -webkit-box-shadow: 5px 5px 5px #777777;
    box-shadow: 5px 5px 5px #777777;}
    p.three {
    -moz-box-shadow: 5px 5px 5px 5px #777777;
    -webkit-box-shadow: 5px 5px 5px 5px #777777;
    box-shadow: 5px 5px 5px 5px #777777;}
    p.four {
    -moz-box-shadow: 0 0 10px #777777;
    -webkit-box-shadow: 0 0 10px #777777;
    box-shadow: 0 0 10px #777777;}
    p.five {
    -moz-box-shadow: inset 0 0 10px #777777;
    -webkit-box-shadow: inset 0 0 10px #777777;
    box-shadow: inset 0 0 10px #777777;}
    (p327)
    ```
  -rounded corners
  ```css
  p {
  border: 5px solid #cccccc;
  padding: 20px;
  width: 275px;
  text-align: center;
  border-radius: 10px;
  -moz-border-radius: 10px;
  -webkit-border-radius: 10px;}

  border-top-right-radius
  border-bottom-right-radius
  border-bottom-left-radius
  border-top-left-radius
  ```

  
