# Class 03 Reading: Passing Functions as Props

## Reading
[React Docs - lists and keys](https://reactjs.org/docs/lists-and-keys.html)

1. What does .map() return?
  - new array, based on input with array.map()

2. If I want to loop through an array and display each value in JSX, how do I do that in React? 
  - must use curly brackets 
  - `<li>{number}</li>` 
  - can then return into a new <ul> element 
  - `<ul>{listItems}</ul>` 

3. Each list item needs a unique ___. 
  - Key
  - often use IDs from data
  ```javascript
  const todoItems = todos.map((todo) =>
  <li key={todo.id}>
    {todo.text}
  </li>
  );  
  ```
  - without stable IDs, use idx
  ```javascript
  const todoItems = todos.map((todo, index) =>
  <li key={index}>
    {todo.text}
  </li>
  );
  ```

4. What is the purpose of a key?
  - help React identify which items have changed, are added, or removed

[The Spread Operator](https://medium.com/coding-at-dawn/how-to-use-the-spread-operator-in-javascript-b9e4a8b06fab)

1. What is the spread operator?
  - use of ellipsis to expand iterable object into list of args
  - 'spreads' arr or obj into separate args
  ```js
  Math.max(...[1,3,4]) //5 vs NaN w.o ...
  ```

2. List 4 things that the spread operator can do.
  - copy an array
  - concatenating or combining arrays
  - using math funcs
  - using an array as args
  - adding an item to a list
  - adding to state in React
  - combining objects
  - converting NodeList to an array

3. Give an example of using the spread operator to combine two arrays.
  ```js
  const hello = {hello: "😋😛😜🤪😝"}
  const world = {world: "🙂🙃😉😊😇🥰😍🤩!"}

  const helloWorld = {...hello,...world}

  console.log(helloWorld) // Object { hello: "😋😛😜🤪😝", world: "🙂🙃😉😊😇🥰😍🤩!" }
  ```

4. Give an example of using the spread operator to add a new item to an array.
```js
  
const fruits = ['🍏','🍊','🍌','🍉','🍍']

const moreFruits = [...fruits];

console.log(moreFruits) // Array(5) [ "🍏", "🍊", "🍌", "🍉", "🍍" ]

fruits[0] = '🍑'

console.log(...[...fruits,'...',...moreFruits]) //  🍑 🍊 🍌 🍉 🍍 ... 🍏 🍊 🍌 🍉 🍍
```

5. Give an example of using the spread operator to combine two objects into one.
```js
const myArray = [`🤪`,`🐻`,`🎌`]
const yourArray = [`🙂`,`🤗`,`🤩`]
const ourArray = [...myArray,...yourArray]
console.log(...ourArray) // 🤪 🐻 🎌 🙂 🤗 🤩
```

## Videos

[How to Pass Functions Between Components](https://www.youtube.com/watch?v=c05OL7XbwXU)

1. In the video, what is the first step that the developer does to pass functions between components?
  - create the function wherever (which component) the state is that's getting changed

2. In your own words, what does the increment function do?
  - receive name, loop through array, find matching array, and update that one
  ```javascript
  increment = (name) => {
    let ppl = this.state.people.map( (p) => {
      if(p.name === name) {
        p.count++;
      }
      return p;
    });
    this.setState({people:ppl});
  }
  ```
3. How can you pass a method from a parent component into a child component?
  - props
  - from parent
    - in render() inside component
      - increment={this.increment}

4. How does the child component invoke a method that was passed to it from a parent component?
  - to child
    - bring in as props
    - this.props.increment() to call

## Bookmark and Review
- [React Tutorial through 'Declaring a Winner'](https://reactjs.org/tutorial/tutorial.html)
- [React Docs - Lifting State Up](https://reactjs.org/docs/lifting-state-up.html)

## Things I want to know more about
- who comes up with the syntax that's required for all this code???