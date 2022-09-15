# Read 19: Automation

## Read
[Python RegEx Tutorial](https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial)
- Brush up on RegEx?
  - compile()
  - search()
  - findall()
  - sub()
  - split()
- `import re`
```
pattern = r"Cookie"
sequence = "Cookie"
if re.match(pattern, sequence):
    print("Match!")
else: print("Not a match!")
```
- match() returns a match object if it is a match, otherwise returns None
  - requries r"" raw string literal
    - keeps backslashes
- search()
  - scan through given string/sequence, look for first location where regular expression produces a match
- group()
  - returns string matched by the re. 
- '.'
  - matches any single character except newline char
- '^'
  - caret matches the start of the string
    - use if you want to make sure something starts with certain chars
- '$'
  - matches end of string
- [a-zA-Z0-9]
  - matches any letter from (a-z)(A-Z)(0-9)
    - compliment set with ^ for 'NOT IN SET' to match
- '\'
  - removes special char
- \w
  - any single letter, digit, or underscore
- \W
  - any character not part of \w

- article appears to continue on to all common chars


[Shutil](https://pymotw.com/3/shutil/)
- shutil module include high-level ops such as copying and archiving
- copyfile() copies contents of source to destination, raises IOError if not permitted to write there
```
import glob
import shutil

print('BEFORE:', glob.glob('shutil_copyfile.*'))

shutil.copyfile('shutil_copyfile.py', 'shutil_copyfile.py.copy')

print('AFTER:', glob.glob('shutil_copyfile.*'))
```

- syntax looks pretty cumbersome at first glance. I'm curious who made this library/module.


- can copy metadata as well
- works with directory trees
- finds files
- Archives
- examines file system space


## Additional Resources

### Video
[Automation Ideas](https://www.youtube.com/watch?v=qbW6FRbaSl0&t=69s)
- cool automation ideas
  - filesystem organization
  - open youtube triggered by new video release
    - open trading site when a stock price changes
  - estimating yearly interest
[Automating Your Browser and Desktop Apps](https://www.youtube.com/watch?v=dZLyfbSQPXI)

## Bookmark and Review
[Watchlog](https://pythonhosted.org/watchdog/)

## Things I'd like to know more about
- how do you make a library/module for pipy
- can you get paid for publishing code for others to use, like libraries and modules, on pipy?
