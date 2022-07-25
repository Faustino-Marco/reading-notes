# Day 1 Readings

## Readings

### [Pain and Suffering](https://codefellows.github.io/code-401-python-guide/curriculum/class-01/notes/pain_suffering)

- Physical, mental, emotional toll
- Pain is not the same as suffering

`Suffering is dependent on the story that we layer on top of our pain`

- Story attached to pain
  - What's your perspective?
  - Why are you doing this?
  - Do you want what comes at the end of this journey?
  - Are you doing this for you?

Remember: I'm here because I chose to invest in a different life. A better life.

Welcome to Code 401.

### [Beginners Guide to Big O](https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/)

- Term used to describe the performance and complexity of an algorithm
  - specifically the worst-case scenario

- O(1)
  - algorithm that will always execute in the same time (or space) regardless of the size of the input data set
```
bool IsFirstElementNull(IList<String> elements)
{
    return elements[0] == null;
}
```

- O(N)
  - algorithm whose performance will grow linearly and in direct proportion to the size of the input data set
```
bool ContainsValue(IEnumerable<string> elements, string value)
{
    foreach (var element in elements)
    {
        if (element == value) return true; 
    }     
    return false; 
}
```

- O(N^2)
  - algo perf proportional to square of size of data set
```
bool ContainsDuplicates(IList<string> elements)
{
    for (var outer = 0; outer < elements.Count; outer++) 
    {
        for (var inner = 0; inner < elements.Count; inner++) 
        { 
            // Don't compare with self 
            if (outer == inner) continue;             
            
            if (elements[outer] == elements[inner]) return true; 
        }
    }    
    return false;
}
```

- O(2^N)
  - algo whose growth doubles with each addition to the input data set
```
int Fibonacci(int number)
{
    if (number <= 1) return number;
       
    return Fibonacci(number - 2) + Fibonacci(number - 1); 
}
```
-Logs
  - binary search used to halve and find median in data set over and over again

## Videos

### [Names and Values in Python](https://www.youtube.com/watch?v=_AEJHKGk9ns)
  - Ned Batchelder
  - Python is 'simple'
  - Names reassigned independently
  - assignment never copies data
    - idk what this means but speaker was adamant
  - immutable values cannot alias
    - mutable/immutable assigned the same
  - lots of things are references (as opposed to names)
    - eg. obj[f]
  - RETURN A NEW LIST (MAKE NEW LISTS)
  - names have no type
    - no scope
  - values have no scope
    - no type
  - see [Pythontutor.com](pythontutor.com)
  - Q/A: 
    - immutable default value
      - held onto by function
      - if use list as func arg
      - will be used for every fn call
        - grows indefinitely

## Additional Resources

### [S1E6: A friendly intro to Big O Notatio](https://www.codenewbie.org/basecs/8)

## Bookmark and Review

### [Awesome Python Environment](https://towardsdatascience.com/how-to-setup-an-awesome-python-environment-for-data-science-or-anything-else-35d358cc95d5)

### [Python Module of the Week](https://pymotw.com/3/index.html)