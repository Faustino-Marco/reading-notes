# Putting it All Together

## Reading 
[React Docs - Thinking in React](https://reactjs.org/docs/thinking-in-react.html)

1. What is the single responsibility principle and how does it apply to components?
- a component should only do one thing
- if a component ends up growing, it should be decomposed into smaller subcomponents
2. What does it mean to build a ‘static’ version of your application?
  - build long way without using state
  - build top-down or bottom-up
    - hierarchy td for simple 
    - bu for large projects
3. Once you have a static application, what do you need to add?
  - apply the use of `state`
4. What are the three questions you can ask to determine if something is state?
  - Is it passed in from a parent via props? 
    - If so, it probably isn’t state.
  - Does it remain unchanged over time?   
    - If so, it probably isn’t state.
  - Can you compute it based on any other state or props in your component? 
    - If so, it isn’t state.

5. How can you identify where state needs to live?

- Identify every component that renders something based on that state.

- Find a common owner component (a single component above all the components that need the state in the hierarchy).

- Either the common owner or another component higher up in the hierarchy should own the state.

- If you can’t find a component where it makes sense to own the state, create a new component solely for holding the state and add it somewhere in the hierarchy above the common owner component.


[Higher-Order Functions](https://eloquentjavascript.net/05_higher_order.html#h_xxCc98lOBK)

1. What is a “higher-order function”?
  - functions that operate on other functions
    - taking them as args or returning them

2. Explore the greaterThan function as defined in the reading. In your own words, what is line 2 of this function doing?
  - comparing function input 'n' to arg in code block 'm'

3. Explain how either map or reduce operates, with regards to higher-order functions.
  - the code blocks of map and reduce are functions within the function that exists as the array.map() or array.reduce() methods
  
## Things I want to know more about
- 