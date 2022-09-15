# Ten Thousand 3

## Read
[List Comprehensions](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)
- Syntax
  - `my_new_list=[expression(1) for item(2) in list(3)]`
    1. expression to carry out
    2. object expression works on
    3. iterable list of objects to build new list from
- create a list with `range()`
  - `digits = [x for x in range(10)]`
- create a list using loops/comprehension
  - append an empty new_array with a for-loop
  - OR
  - `new_arr = [x**2 for x in range(10)]`
- multiplication
  - `m3 = [x*3 for x in range(10)]`
- first letter of names
  - `letters = [ name[0] for name in auth ]`
- .lower()
  - `lower = [letter.lower() for letter in arr]`
- if statements
  - print numbers only
    - `phone = [ x for x in data if x.isdigit()]`
- parsing
  ```
  # open the file in read-only mode
  file = open("dreams.txt", 'r')
  poem = [ line for line in file ]

  for line in poem:
    print(line)
  ```
- adding args to list comp
  - `nums = [double(x) for x in range(1,10)]

- basically looks like you replace x in list with newly defined x or whatever you do to x

## Audio
[Debugging with PySnooper](https://www.pythonpodcast.com/pysnooper-python-debugging-episode-241/)

## Bookmark and Review
[Primer on Decorators](https://realpython.com/primer-on-python-decorators/)
