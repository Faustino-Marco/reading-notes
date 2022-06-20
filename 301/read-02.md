# Class 02 Reading: State and Props

## Reading
[React lifecycle](https://medium.com/@joshuablankenshipnola/react-component-lifecycle-events-cb77e670a093)

  - Mounting
    - Constructor, static getDerivedStateFromProps, render, componentDID  Mount, and UNSAFE_componentWillMount
    - Updating
      - any time a component or state changes it is rerendered (in this order:)
      - static getDerivedStateFromProps, shouldComponentUpdate, render, getSnapshotBeforeUpdate, componentDidUpdate, UNSAFE_componentWillUpdate, UNSAFE_componentWillReceiveProps
    - Unmounting
      - final phase of the lifecycle if called when a component is being removed from the DOM
        - componentWillUnmount is only l-c event during this phase
    - consturctor()
      - called before mounted
      - if subclass--call super(props)
      - can be used to assign state using this.state or to bind event handle methods to an instance
      - AVOID using `this.setState()` in constructor
        - can lead to side effects, unnecessary
        - will ignore all updates from props
    - static getDerivedStateFromProps()
      - rare case where the state relies on changes in props over time
    - render()
      - only required method in a class component
      - examines this.props and this.state when called
      - should not modify the component state!
      - should not directly interact with the borwser
        - will not be invoked if shouldComponentUpdate() returns false
    - componentDidMount()
      - invoked immediately after a component is mounted
      - load anything using a network request or initialize the DOM
      - good place to set up any subscriptions
        - don't forget to unsubscribe in componentWillUnmount()
    - shouldComponentUpdate()
      - if set to false--stops rerendering after change to state
        - if returns false: 
          - UNSAFE_ComponentWillUpdate(), render(), and componentDidUpdate() will NOT be invoked
      - in order to optimize performance
      - consider using PureComponent instead
        - performs shallow comparison of porps and state
    - getSnapshotBeforeUpdate()
      - rarely used
      - allows you to capture a picture of the DOM to check it before actually changing anything on the DOM
    - componentDidUpdate()
      - useful for performing network requests after a change has occurred
      ```javascript
      componentDidUpdate(prevProps) {
      // Typical usage (don’t forget to compare props):
      if (this.props.userID !== prevProps.userID) {
      this.fetchData(this.props.userID);
      }
      }
      ```
    - componentWillUnmount()
      - allows you to clean up the DOM and network requests/subscriptions


1. Based off the diagram, what happens first, the ‘render’ or the ‘componentDidMount’?
    - Render

2. What is the very first thing to happen in the lifecycle of React?
    - Mounting

3. Put the following things in the order that they happen: componentDidMount, render, constructor, componentWillUnmount, React Updates
    - Constructor, render, react updates, component did mount, componentWillUnmount

4. What does componentDidMount do?
    - invoked immediately after component is mounted
    - setState() can technically be called here but SPARINGLY

## Videos
[React State Vs Props](https://www.youtube.com/watch?v=IYvD9oBCuJI)

1. What types of things can you pass in the props?
  - Things to initialize or to render
  - state, initial 'count' for counter function
  - titles, subtitles
  - 

2. What is the big difference between props and state?
  - props are passed 'into' a component
  - state is handled inside of the component
  - props are handled outside of the component
  - state is very useful inside of a form

3. When do we re-render our application?
  - Whenever state changes

4. What are some examples of things that we could store in state?
  - initial values, args, things to be updated (outside the component)

- pass info into component using props if it will change outside the component

## Bookmark & Review
- [React Docs - State and Lifecycle](https://reactjs.org/docs/state-and-lifecycle.html)
- [React Docs - handling events](https://reactjs.org/docs/handling-events.html)
- [React Tutorial through 'Dev Tools'](https://reactjs.org/tutorial/tutorial.html)
- [React Bootstrap Docs](https://react-bootstrap.github.io/)
- [Bootstrap Cheatsheet](https://getbootstrap.com/docs/5.0/examples/cheatsheet/)
- [Bootstrap Shuffle - a class 'sandbox'](https://bootstrapshuffle.com/classes)
- [Netlify](https://www.netlify.com/)

## Things I want to know more about
- I'm a little confused still about state/props but I'm confident that it will begin to make more sense as we move forward.