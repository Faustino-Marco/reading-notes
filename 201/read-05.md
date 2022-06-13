# READ 05

## HTML IMAGES

- Stock Photos
  - [istock](www.istockphotos.com)
  - [getty](www.gettyimages.com)
  - [veer](www.veer.com)
  - [sxc](www.sxc.hu)
  - [fotolia](www.fotolia.com)

- keep in separate folder to access in code
`<img src="" alt="" title="">`
- height / width can be included in tag
- Where to place
  - before <p>
  - inside start of <p> tag
  - middle of <p>
  - align left, right, top or bottom with <p>'s

- 3 rules for creating images
  - save images in the right format
    - might not look as sharp
  - save images at the right size
    - same width and height as on source site
  - use the correct resolution
    - 72px/in is standard
    - higher res means bigger and slower

- formats
  - jpeg
    - many different colors
  - gif
    - use gif or png when saving images with few colors or large areas of same color
      -logos, illustrations, diagrams, (flat colors)
  - see p(118) for opaque/translucense

- Examine on web
  - chrome
    - open in new tab
    - save image as
  - firefox
    - view image info

## CSS COLOR

- Foreground Color
  - RGB
  - HEX
  - Color names

- background color
  - background-color: value;

- adjustments
  - can adjust contras, hue, saturation, brightness

- opacity
  - opacity: 0.5;
  - HSL notation

## TEXT 

- typeface terms
  - serif
    - georgia
    - times
    - times new roman
  - sans serif
    - arial
    - verdana
    - helvetica
  - monospace (typewriter)
    - courier
    - courier new
  - weight
    - comic sans ms
  - style
  - stretch
  - cursive
    - monotype corsica
    - comic sans ms
  - fantasy
    - impact
    - haettenschweiler
  - `font-family`, `font-face`, `service-based font-face`, 
    - give wider choices
- type size
  - pixels
    - XXpx
  - percent
    - 200% of 16px
  - em's
    - body is 16px, 1.0em
  - line-height
    - single/double space
  - letter/word spacing
  - text-align
    - left, right, center
  - justify
    - regulates all lines possible full width
  - vertical align
  ```css
  #six-months {
  vertical-align: text-top;}
  #one-year {
  vertical-align: baseline;}
  #two-years {
  vertical-align: text-bottom;}
  ```
  - indenting text negative 9999
  - drop shadow
    - higher values get more shadow
  - first-letter, first-line;
  - Styling links
    - :link {}
    - :visited {}
  - :hover{}
    - hovers over an element with mouse
  - :active {}
    - applied when activated by user
      - so it looks feels like pressed
  - :focus {}
  - attribute selectors
    - existence, equality, space, prefix, substring, suffix





