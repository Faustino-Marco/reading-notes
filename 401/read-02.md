# Testing and Modules

## Reading
### [In Tests We Trust](https://code.likeagirl.io/in-tests-we-trust-tdd-with-python-af69f47e6932)
- Unit Tests
  - pieces of code to exercise the input, output, and behavior of code
  - can write them anytime
- TDD (Test-Driven Development)
  - Strategy: consider and write tests first.
```
def test_should_return_female_when_the_name_is_from_female_gender():

    detector = GenderDetector()

    expected_gender = detector.run(‘Ana’)

    assert expected_gender == ‘female’
```
  - Test Name
    - be very descriptive 
    - 'alive documentation'
    - should follow module name
    - separate tests folder from production code
  - AAA (Arrange, Act, Assert)
    - Arrange
      - organize data needed to execute
    - Act
      - execute code being tested
    - Assert
      - check if result/output is same as expected
  - The Cycle
    - Write unit test
      - make it fail to test
    - Write feature
      - make it pass
    - Refactor code
      - clean after working 

### [If name equals main](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)
-  interpreter assigns value to __name__ variable when reading code.
- value assigned is __main__ if reading that code directly, as opposed to as a module.
- can use to test if writing code designed to be used as a module & vise/versa
- if __name__ == "__main__" then module is being run standalone by the user
- if imported as a module in another script, __name__ is set to the name of the script/module

### [Recursion](https://www.geeksforgeeks.org/recursion/)

## Videos
### [What on Earth is Recursion](https://www.youtube.com/watch?v=Mv9NEXX1VHc)
- demonstrated using stack model
- uses argument/parameter with multiple different values all at once
- anchored out of infite scope with base variable setting ie. `x == 1`

## Bookmark and Review
#### [Google for Education: Python Lists](https://developers.google.com/edu/python/lists)

#### [Google for Education: Python Strings](https://developers.google.com/edu/python/strings)

#### [Python Modules and Packages](https://realpython.com/python-modules-packages/)

#### [PyTest Documentation](https://docs.pytest.org/en/latest/)

#### [PyTest Tutorial](https://www.guru99.com/pytest-tutorial.html) 
(Up to section, 'Running tests in parallel')

