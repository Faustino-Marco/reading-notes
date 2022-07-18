# CRUD

## Reading

[Status Codes Based on REST Methods](https://www.moesif.com/blog/technical/api-design/Which-HTTP-Status-Code-To-Use-For-Every-CRUD-App/)

1. In your own words, describe what each group of status code represents.
- 100's
  - informational: like a quick update midway through processing
- 200's
  - success codes
    - sometimes just about meeting requirements (202) and not necessarily successful process 
- 300's
  - redirection codes
    - resource requested isn't available at the expected location anymore
- 400's
  - client error codes
    - invalid requests the client sent to server
      - timeouts, wrong URI, missing auth, etc.
- 500's
  - server error codes
    - overwhelmed servers, unreachable behind proxies
      - sometimes directly related to client requests
2. What is a status code 202?
  - requirements for inquiry met, but not necessarily successful
3. What is a status code 308?
  - permanent redirect
4. What code would you use if an update didn't return data to a client?
  - 400's if because of client side
  - 500's if because of server side
5. What code would you use if a resource used to exist but no longer does?
  - 410? gone?
6. What is the 'Forbidden' status code?
  - 403

## Videos

[Build a REST API with Node.js, Express, & MongoDB - Quick](https://www.youtube.com/channel/UCFbNIlppjAuEX4znoulh0Cw)

1. Why do we need to pull our MongoDB database string out of our server and put it into our .env?
  - private info, not to be pushed publicly
2. What is middleware?
  - functionality that exists, or at least gets invoked and operates, within the bounds of requests and responses.
3. What does `app.use(express.json())` do?
  - allows express to interpret .json data
4. What does the `/:id` mean in a route?
  - this is similar to variable declaration
5. What is the difference between PUT and PATCH?
  - 
6. How do you make a default value in a schema?
  - set a string like `name` or `status` to an object with `type: type` and `required: boolean` in JSON
  ```js
  const mySchema = new mongoose.Schema ({
    name: {
      type: String,
      required: true
    },
    height: {
      type: Number,
      required: true
    }
  })
  ```
7. What does a 500 error status code mean?
  - server error
8. What is the difference between a status 200 and a status 201?
  - 200 is success in general and 201 is Successfully created and object (post route)

## Things I want to know more about
- this video requires mongoose and express a little differently than we do it. I'm curious to know if industry standard leans more in either direction (more variable declaration on more lines, or more consolidation vertically with longer lines of code without using variables and substitutions)