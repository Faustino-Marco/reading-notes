# READ 11: ASSORTED TOPICS

## IMAGES

- aligning images
```css
img.align-left {
float: left;
margin-right: 10px;}
img.align-right {
float: right;
margin-left: 10px;}
img.medium {
width: 250px;
height: 250px;}
```
- centering images
```css
img.align-center {
display: block;
margin: 0px auto;}
img.medium {
width: 250px;
height: 250px;}
```

- background images
```css
body {
background-image: url("images/pattern.gif");}```
- background-position: center top;
- shorthand
```css
body {
background: #ffffff url("images/tulip.gif")
 no-repeat top right;}
```
- repeating images
  - repeat-x; repeat-y; fixed, scroll

gradients
  - not supported by all browsers

## Practical Information

- SEO p.480
  - trying to help site get more traffic/visibility
  - on-page
    - title
    - url/web address
    - headings
    - text
    - link text
    - image alt text
    - page descriptions

- analytics
  - signing up
  - how it works
  - tracking code
    - visits
    - unique visits
    - page views
    - pages per visit
    - average time on site
    - date selector
    - export
  - pages
    - landing pages
    - top exit pages
    - bounce rate
      - leave from page user arrived at
  - viewership
    - referrers
    - direct
    - search terms
    - advanced features
  - domain names and hosting
    - domain names
      - web address you can own
    - web hosting
      - launch from web server
    - disk space, bandwidth, backups
  - FTP (file transfer protocol)
    - lots of ftp services on web

## AUDIO / VIDEO API'S

- Video and audio elements in html
```js
<video controls>
  <source src="rabbit320.mp4" type="video/mp4">
  <source src="rabbit320.webm" type="video/webm">
  <p>Your browser doesn't support HTML5 video. Here is a <a href="rabbit320.mp4">link to the video</a> instead.</p>
</video>
```
- need some software but coding video elements in can be done

- controls styling
```js
.controls {
  visibility: hidden;
  opacity: 0.5;
  width: 400px;
  border-radius: 10px;
  position: absolute;
  bottom: 20px;
  left: 50%;
  margin-left: -200px;
  background-color: black;
  box-shadow: 3px 3px 5px black;
  transition: 1s all;
  display: flex;
}

.player:hover .controls, 
.player:focus-within .controls {
  opacity: 1;
}
```

- use the dom to access html with image/video links

mdn link to build video player? 
[mdn-img&video](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Video_and_audio_APIs)







