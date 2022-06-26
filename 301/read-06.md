# NODE.JS

## Reading
[An Intro to Node on Sitepoint](https://www.sitepoint.com/an-introduction-to-node-js)

1. What is node.js?
  - javascript runtime built on chrome's v8 js engine
  - event-based, non-blocking, asynchronous I/O runtime that uses goog...

2. In your own words, what is Chrome's V8 JavaScript Engine?
  - open-source JS engine runs in google chrome & others (Brave, Opera, Vivaldi, etc.)
  - designed with performance in mind
  - compiles JS directly to native machine code 
3. What does it mean that node is a JavaScript runtime?
  - node enhances the v8 engine with features
    - file system API
    - HTTP library, os-related utility methods
4. What is npm?
  - package manager that comes bundled with node
  - npm package
    - somebody else's code
5. What version of node are you running on your machine?
  - v18.3.0
6. What version of npm are you running on your machine?
  - v8.11.0
7. What command would you type to install a library/package called 'jshint'?
  - npm install -g jshint

8. What is node used for?
  - installing and running various build tools
  - designed to automate the process of developing a modern JS app

[6 Reasons for Pair Programming](https://www.codefellows.org/blog/6-reasons-for-pair-programming/)

1. What are the 6 reasons for pair programming?
  - Greater efficiency
  - Engaged Collaboration
  - Learning from fellow students
  - Social Skills
  - Job interview readiness
  - work environment readiness

2. In your experience, which of these reasons have you found most beneficial?
  - Engaged collaboration has lead to even higher highs when I've finally written a functioning piece of code with someone else. There's another stakeholder in the (virtual) room to celebrate with, and to encourage or pick me up when I'm just slogging through the code.

3. How does pair programming work?
  - Typically two people, one driver one navigator
    - driver is programmer
    - navigator uses words to guide driver

## Bookmark and Review
- [Geocoding API Docs](https://locationiq.com/)
- [Axios docs](https://www.npmjs.com/package/axios)
- [MDN async and await](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Async_await)
- [error dogs](httpstatusdogs.com/)

## Things I want to know more about
- What are some cool games or software you can download with npm 

## Class 06 lecture notes

### Axios
  - asynchronous
  below is unfinished
    - async, await, .data

  ```js

  class App extends React.Component {
  constructor(props);
  super(props);

  handleSubmit = async (event) => {
    event.preventDefault();
    //make a request to the SW API and get data
    let starWarsCharacters = await axios.get('https://swapi.dev/api/people/?page=1');
    //proof of life
    console.log(starWarsCharacters.data.results);
    // save the data in state
    this.setState({
      starWarsChars: starWarsCharacters.data.results
    });
  };

  handleCityInput = (e) => {
    this.setState({
      city: e.target.value
    });
  };

  handleCitySubmit = async (e) => {
    e.preventDefault();
    // make request to my API using data from state
    // template literals for api key and search value
    let url = `https://us1.locationiq.com/v1/search.php?key=${process.env.REACT_APP_LOCATIONIQ_API_KEY}&q=${this.state.city}&formate=json`;
    let cityInfo = await axios.get(url);
    console.log(cityInfo.data[0]);
  };

  render() {
    console.log(this.state.starWarsChars);
    let starWarsList = this.state.starWarsChars.map((character) => {
      return <li>{character.name}</li>;
    });

    return (
      <>
      <h1></h1>
      <form onSubmit={this.handleSubmit}>
        <button> type="submit"> Display Star Wars Characters </button>
      </form>
      <ul>
      {starWarsList}
      </ul>
      <form onSubmit={this.handleCity}>
        <label>Pick a City:
          <input type="text" onInput={this.handleCityInput}>
        </label>

      </>
    );
  };
  };
  ```

  ### API keys
  - add .env file (your actual API key)
    - set to variable
  - add .env.sample file (user key)
  - RESTART SERVER EVERY TIME YOU CHANGE .ENV

  ### DON'T FORGET
   - chrome JSON Formatter extension

   ## LAB 06
    - errors
      - at request to api
        - wrap entire block in try{}
        - then catch (error) {} like `else`
          - 