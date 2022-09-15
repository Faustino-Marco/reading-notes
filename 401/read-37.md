# React 1

## ES6 Overview
[ES6 Syntax and Feature Overview](https://www.taniarascia.com/es6-syntax-and-feature-overview/)
- Not a standalone article
- Standard Overview / Docs
    - See Table of Contents
## React
[Hello World](https://reactjs.org/docs/hello-world.html)
```JS
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<h1>Hello, world!</h1>);
```

- 

[JSX](https://reactjs.org/docs/introducing-jsx.html)
```js
const element = <h1>Hello, world!</h1>;
```

- 

[Rendering Elements](https://reactjs.org/docs/rendering-elements.html)
- Rendering an Element into the DOM
    - first pass the DOM element to ReactDOM.createRoot()
    - then pass the React element to root.render()

```js
const root = ReactDOM.createRoot(
  document.getElementById('root')
);
const element = <h1>Hello, world</h1>;
root.render(element);
```

- Updating...

[Components and Props](https://reactjs.org/docs/state-and-lifecycle.html)
- 
[State & Lifecycle](https://reactjs.org/docs/state-and-lifecycle.html)
[Handling Events](https://reactjs.org/docs/handling-events.html)

## Tailwind CSS
[Utility First CSS](https://tailwindcss.com/docs/utility-first)
[Tailwind in 15 Minutes](https://www.youtube.com/watch?v=6zIuAyLZPH0)

## Next.js
[Learn Next.js](https://nextjs.org/learn/basics/create-nextjs-app)
[Why to use Next.js](https://www.youtube.com/watch?v=rtgbaKBhdkk)
