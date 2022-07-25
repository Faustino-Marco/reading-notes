# File IO & Exceptions

## Reading

- [Read & Write Files in Python](https://realpython.com/read-write-files-python/)
  - What is a File?
    - Paths
      - path / unix, \ windows
      - name
      - ext .txt, .png. etc
    - 3 main parts
      - Header
        - metadata about contents
          - name, size, type, etc
      - Data
        - contents of file
      - End of File (EOF)
        - special character indicating EOF
    - line endings
      - ISO (int'l org for stndrd'n)
        - \r or \n required
      - ASA (american stndrd assn)
        - \r\n required
    - Character encodings
      - encoding of byte data
      - assigning numerical value to represent a character
      - most common
        - ASCII (128 chars)
        - UNICODE aka UTF-8 (1,114,112 chars)
  - Opening and closing a file in Python
    ```
    reader = open('dog_breeds.txt')
    try:
      # Further file processing goes here
    finally:
      reader.close()
    ```
    - modes
      - r
        - read
      - w
        - write
      - rb / wb
        - read byte data / write byte data
    - file objects
      - text files
        - open('abc.txt')
        - open('abc.txt', 'r')
        - open('abc.txt', 'w')
        - `>>> file = open('dog.txt')`
        - `>>> type(file)`
        - `<class '_io.TextIOWrapper'>`
      - buffered binary files
        - open('abc.txt', rb)
  - Read
    - `.read(size=-1)`
      - reads fro file based on number of size bytes
        - none or -1 read entire file
    - `.readline(size=-1)`
      - none or -1 read entire/rest of line
    - `.readlines()`
      - reads remaining lines and RETURNS THEM AS LIST
  - Write
    - `.write(string)`
    - `.writelines(seq)`
      - writes the sequence to the file
        - no line endings added, up to you
```
with open('dog_breeds.txt', 'r') as reader:
    # Note: readlines doesn't trim the line endings
    dog_breeds = reader.readlines()

with open('dog_breeds_reversed.txt', 'w') as writer:
    # Alternatively you could use
    # writer.writelines(reversed(dog_breeds))

    # Write the dog breeds to the file in reversed order
    for breed in reversed(dog_breeds):
        writer.write(breed)
```
      - see dos2unix.py
  - Tips and Tricks
    - `__file__`
      - pathname of file from which module was loaded, if loaded from a file
    - append to a file
      - `with open('dog.txt', 'a') as a_writer:`
        - `a_writer.write('\nBeagle')`
      - simultaneous
```
d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))
```
  - see article for other file type details
    
- [Exceptions in Python](https://realpython.com/python-exceptions/)
  - syntax error
    - parser detects and incorrect statement
  - exception error
    - code is syntactically correct
    - but there's an error
  - raising exceptions
    - `raise Exception('text {}'.format(x))`
    - assert in testing raises its own error
    - try/except block
      - else: clause
        - print only in absence of exceptions
      - finally block (always runs)

## Videos

- [Read & Write Files in Python - Companion Video](https://realpython.com/courses/reading-and-writing-files-python/)

## Bookmarks and Review

- [Reading and Writing Files in Python Quiz](https://realpython.com/quizzes/read-write-files-python/)

## Things I want to know more about
  - I want to get into automating file writing! Looking forward to it.