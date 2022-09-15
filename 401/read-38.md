# React 2

## Reading
[Conditional Rendering](https://reactjs.org/docs/conditional-rendering.html)
- use of operators like `if` or the `conditional operator`
- react updates the UI to match


[Lists & Keys](https://reactjs.org/docs/lists-and-keys.html)
- react transforms lists almost exactly how it's done in JS
- a `key` is a string attribute that needs to be included when creating a list of elements.
    - key goes into the tag
        - `<li key={number.toString()}>{num}</li>`


[Forms](https://reactjs.org/docs/forms.html)
- Controlled components
    - HTML updates based on input
        - input
        - textarea
        - select

    - in react use `setState()`
        - `handleChange`
        - `handleSubmit`


[Lifting State](https://reactjs.org/docs/lifting-state-up.html)
- lift shared state up to closest common ancestor of components that share the same changing data


[Composition vs Inheritance](https://reactjs.org/docs/composition-vs-inheritance.html)
- use compositino instead of inheritance to reuse code between componenets
- some components don't know their children ahead of time
    - generic boxes
    - use special `children` prop to pass children elements directly into their output


[Thinking In React](https://reactjs.org/docs/thinking-in-react.html)
- start with mock
- JSON API example
    - break into component hierarchy
    - USE THIS RESOURCE FOR PROJECT


## Bookmark & Review
[React - Comprehensive Guide](https://tylermcginnis.com/reactjs-tutorial-a-comprehensive-guide-to-building-apps-with-react/)


## TIWKMA
- The example in "Thinking in React" highlights a JSON API, I'd love to see an example of the same operations being done with a relational database.