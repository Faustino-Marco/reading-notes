# CHART.JS, CANVAS

## Chart.js API

- js plugin using html5's canvas element to draw the graph onto the page
- download chart.js
- copy chart.min.js
- import script
- various types of charts. Code available [here](https://www.webdesignerdepot.com/2013/11/easily-create-stunning-animated-charts-with-chart-js/).

- Chart.js docs [here](https://www.chartjs.org/docs/latest/).

## CANVAS
- The Canvas Element:
```html
<canvas id="tutorial" width="150" height="150"></canvas>
```
- similar to img element
- fallback content
  - flexible in browsers that do/don't use/read the canvas element
- required closing `</canvas>` tag
- Rendering context
  - initially blank
  - creates a fixed-size drawing surface that exposes one or more rendering contexts, which are used to create and manipulate the content shown.

  ```html
  <!DOCTYPE html>
  <html>
  <head>
  <meta charset="utf-8"/>
  <script type="application/javascript">
    function draw() {
      var canvas = document.getElementById('canvas');
      if (canvas.getContext) {
        var ctx = canvas.getContext('2d');

        ctx.fillStyle = 'rgb(200, 0, 0)';
        ctx.fillRect(10, 10, 50, 50);

        ctx.fillStyle = 'rgba(0, 0, 200, 0.5)';
        ctx.fillRect(30, 30, 50, 50);
      }
    }
  </script>
  </head>
  <body onload="draw();">
   <canvas id="canvas" width="150" height="150"></canvas>
  </body>
  </html>
  ```

- Drawing shapes with canvas [here](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes)

- Applying styles and colors [here](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Applying_styles_and_colors)

- Drawing text [here](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_text)






