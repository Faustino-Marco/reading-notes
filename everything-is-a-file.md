# Everything Is A File! 

In Linux, everything is a file.
- files
- directories
- keyboard is a readonly file

## Linux is an ***Extensionless*** System 

- file.exe - an executeable file, or program
- file.txt - plain text file
- file.png, file.gif, file.jpg - image

Linux doesn't need files to have extensions like windows. 

Linux ignores the extension and looks inside the file to determine what type of file it is.

There is a command called `file` we can use to find out what type of file a certain file is. 
```
file[path] 
``` 

> LINUX IS CASE SENSITIVE! It is possible to have files of the same name but variance in case for different letters. 

Spaces are allowed in file names, so be careful in the command line, use quotes or backslash escapes to solve this

Pro Tip: Tab completion will automatically excape any spaces in the name for you.

