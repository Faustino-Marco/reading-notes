# APIs

## Reading
[API Design Best Practices](https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design)

1. What does REST stand for?
  - proposed in 2000 by Roy Fielding
  - Representational State Transfer
    - architechtural style for building distributed systems based on hypermedia.
2. REST APIs are designed around a ___.
  - <em>resources</em>
  - any kind of object, data, or service that can be accessed by the client.
3. What is an identifier of resource? Give an example.
  - URI--like a url
4. What are the most common HTTP verbs?
  - GET, POST, PATCH, DELETE
5. What should the URIs be based on?
  - <em>nouns</em> or resources (not verbs (operations))
6. Give an example of a good URI.
  - `https://adventure-works.com/orders`
7. What does it mean to have a 'chatty' web API? Is this a good/bad thing?
  - to be avoided - expose a large number of small resources
  - instead: denormalize the data and combine related info into bigger resources
  - this way a single request can get data
8. What status code does a successful `GET` request return?
  - HTTP status code 200 (OK)
9. What status code does an unsuccessful `GET` request return?
  - 404 -- NOT FOUND
  - 204 -- FOUND BUT NO CONTENT
  - 400 -- BAD REQUEST (invalid data in req)
10. What status code does a successful `POST` request return?
  - 201 (CREATED)
11. What status code does a successful `DELETE` request return?
  - 204 -- NO CONTENT


## Bookmark and Review

[RegExr (See: Cheatsheet)](https://regexr.com/)

[RegEx Tutorial](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)

[RexEx 101](https://regex101.com/)
  - used for code challenge RegEx
    - bottom right and bottom left indexes are helpful for finding what you need to use

## Things I want to know more about

- I remember Audrey saying RegEx is used a lot in Python, I'm curious to know what else is possible with RegEx as it seems like an (albeit confusing) exceptionally powerful tool.