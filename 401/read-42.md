# Pythonisms

## Reading
[Dunder Methods](https://dbader.org/blog/python-dunder-methods)
- set of predefine methods to "enrich" your classes
- `__init__()` or `__str__()`
- also called magic methods
- `__getitem__`
    - allows use of Python's list slicing syntax: `obj[start:stop]`
- `__init__`
    - object initialization
        - constructor
        - lets us create objects from the class
        - self.owner = owner, self.amount = amount, etc
    - THIS IS WHY WE CAN HAVE INPUTS FOR OUR OBJECTS! #mindblown
- `def __reversed__(self)`
    - `return self[::-1]`

- operator overloading for comparing accounts
    - this is crazy too
    - explains how comparison operators work under the hood
- 


[Iterators](https://dbader.org/blog/python-iterators)
- This is the most abstract material I've seen in a while. 
- I read it all and I dont really know what to make of it even now. 
- The dunder method stuff was cool but this article is going completely over my head.


[Generators](https://dbader.org/blog/python-generators)
- And this one is even worse. 


## Videos
[What are Generators](https://realpython.com/lessons/what-are-python-generators/)


## Bookmark & Review
[Decorators](https://realpython.com/primer-on-python-decorators/)

## TIWKMA
- very much looking forward to getting JB's explanation of what the heck is going on in these articles since I'm confident he'll be able to break it down better than what I'm getting from the text so far haha