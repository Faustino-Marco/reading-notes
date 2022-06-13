# READ 08: MORE CSS LAYOUT

## LAYOUT

- A brief history
  - 96
    - css1
  - 98
    - css2
  - 2010
    - css3
      - responsive web design
  - 2012
    - media queries
    - flexbox
  - 2017
    - grid
  - 2019
    - intrinsic web design
  - 2021
    - container queries

- display property
```css
.my-element P
display: inline;
```
  - inline elements behave like words in a sentence
  - block elements create new lines for themselves
  - flex
    - makes the box a block level box
    - converts its children to flex items
    - aligns children next to each other in the inline direction
    - stretches children in the block direction
    - will stay on same axis, not wrap
      - change using 
        - align-items: center; justify-content: space-between; flex-wrap: wrap;
  - grid
    - similar to flexbox, but designed to control multi-axis layouts instead of single-axis layouts (vert/horiz)
    - one row:
  ```css
  .my-element {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1rem;
  }
  ```

    - basic multi-axis layout
  ```css
  .my-element :first-child {
  grid-row: 1/3;
  grid-column: 1/4;
  }

  .my-element {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 1rem;
  max-width: 500px;
  }
  ```
  - floats
    - following elements adjusted
    - floated wrapped around in specified direction
  - position
    - relative/absolute
  

  ch. 15: see [Read 04](read-04.md)









