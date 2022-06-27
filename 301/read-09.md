# Functional Programming

## Reading 
[Functional Programming Concepts](https://medium.com/the-renaissance-developer/concepts-of-functional-programming-in-javascript-6bc84220d2aa)

1. What is functional programming?
  - paradigm
  - style of buidling the structure and elements of computer programs
  - treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data
2. What is a pure function and how do we know if something is a pure function?
  - returns same result if given same args
    - no use of external obj or var
  - doesn't cause observable side effects
    - no modifiying global obj or params
3. What are the benefits of a pure function?
  - easier to test
  - expect same result every time
4. What is immutability?
  - unchanging over time or unable to be changed
  - state cannot be changed for immutable data
5. What is Referential transparency?
  - can be replaced with its equivalent

## Videos
[Node JS Tutorial for Beginners #6 - Modules and require()](https://www.youtube.com/watch?v=xHLd36QoS4k)

1. What is a module?
  - logical divisions of code
  - separated by functionality/utility
2. What does the word `require` do?
  - similar to `import` in js react- brings mods in
3. How do we bring another module into the file we are working in?
  - using require('/path')
4. What do we have to do to make a module available?
  - in mod
    - module.exports = whatever we'd like to use externally;
  - in app 
    - set var name of requre() to exports

## Things I want to know more about

- I'm looking forward to putting this to use to clean up my code! Not sure how it'll all work out but I'm sure it will be so satisfying to get a nicely cleanup piece of code going. 