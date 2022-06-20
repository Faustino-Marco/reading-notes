# React and Forms

## Reading 
[React Docs - Forms](https://reactjs.org/docs/forms.html)

1. What is a 'Controlled Component'?
  - input form element whose value is controlled by React
  - component that renders for also controls what happens in that form on subsequent input
```js
class NameForm extends React.Component {
constructor(props) {
  super(props);
  this.state = {value: ''};

  this.handleChange = this.handleChange.bind(this);
  this.handleSubmit = this.handleSubmit.bind(this);
}

handleChange(event) {
  this.setState({value: event.target.value});
}

handleSubmit(event) {
  alert('A name was submitted: ' + this.state.value);
  event.preventDefault();
}

render() {
  return (
    <form onSubmit={this.handleSubmit}>
      <label>
        Name:
        <input type="text" value={this.state.value} onChange={this.handleChange} />
      </label>
      <input type="submit" value="Submit" />
    </form>
  );
}
}
```

2. Should we wait to store the users responses from the form into state when they submit the form OR should we update the state with their responses as soon as they enter them? Why?
  - every keystroke
  - can pass to other UI elements

3. How do we target what the user is entering if we have an event handler on an input field?
  - `this.setState((value: event.target.value));`

[The Conditional (Ternary) Operator Explained](https://codeburst.io/javascript-the-conditional-ternary-operator-explained-cac7218beeff)

1. Why would we use a ternary operator?
  - shortens long block of code
  - only need one line with ternary operator

2. Rewrite the following statement using a ternary statement
```javascript
if(x===y) {
  console.log(true);
} else {
  console.log(false);
}
```
- `same = x===y ? console.log(true) : console.log(false);`

## Bookmark and Review
- [React Bootstrap - Forms](https://react-bootstrap.github.io/forms/overview/)
- [React Docs - conditional rendering](https://reactjs.org/docs/conditional-rendering.html)

## Things I want to know more about 
- not sure if my code is correct above for writing my own ternary for the x === y function