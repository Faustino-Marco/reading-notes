# Classes and Objects

## Readings

### [Classes and Objects](https://www.learnpython.org/en/Classes_and_Objects)
- Classes
  - templates to create your objects
- dot notation to access 
  - class().variable
  - class().function
- call __init__(self, etc) to assign values

- dictionaries
  - store using bracket notation
  - or curly braces and key:value pairs
  - use array exctraction notation with %s (var, var)
  - delete using del dict[idx]



### [Thinking Recursively](https://realpython.com/python-thinking-recursively/)
- dividing up santa's work
- assigning 4 houses to elves who can appoint two elves to do their deliveries
  - 1: 4
  - 2: 2
  : 2: 1
```
houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

# Each function call represents an elf doing his work 
def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)
```
- recursion in Python
  - recursive case
  - base case

- recursive data structures
  - list 
    - adding new values to head in list creating new list
- naiive recursion is naiive 
  - fibonacci recursion recaculates same values over and over again
  - use recursive function to cut through recalculating every one explicitly
- mutable data structures don't support structural sharing
  - treating them like immutables is bad for space/GC
- check recursion limit: 
```
import sys
sys.getrecursionlimit()
```

### [Pytest Fixtures and Coverage](https://www.linuxjournal.com/content/python-testing-pytest-fixtures-and-coverage)
- Fixtures 
  - data shared across tests  
  - might involve network or filesystem
  - mark with decorator
  ```
  @pytest.fixture
def simple_file():
   return StringIO('\n'.join(['abc', 'def', 'ghi', 'jkl']))
  ```
  - like creating a sample variable for tests
  - still a function too
    - can make calculations and decisions
      - set scope='module' as param
- Coverage
  - package pytest-cov on PyPI
  - pytest --cov-mymul
  - coverage html
  - creates directory
    - web-based report showing in red where coverage is lacking
## Bookmark and Review

### [Pytest Fixtures](https://docs.pytest.org/en/latest/fixture.html)