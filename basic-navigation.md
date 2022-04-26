# Basic Navigation

This is my notepage from the *Basic Navigation* article. 

[Here](https://ryanstutorials.net/linuxtutorial/navigation.php)'s the link to the article.

## Commands

- pwd
    - this command tells you where you are in the terminal, or which directory you're in.
- ls
    - this displays what directories are inside the one you're currently in (list) 

- ls [options][location] 

    - ls command has more to it that `pwd` 

    - command `ls -l` gives you a "long listing" 

        - first character "-" indicates normal file 
        - first character "d" indicates directory 
        - next 9 characters are permissions for the file or directory 
        - next field is the number of blocks 
        - next field is owner of file or directory 
        - next field is group the -/d belongs to 
        - following is the file size 
        - next is file modification time 
        - finally the actual name of -/d 
    - command `ls /etc` lists /etc's contents instead of the contents of the current directory
    - command `ls -l /etc` shows a long list of the /etc directory 

## Paths 

Whenever we refer to a file or a directory on the command line, we are referring to a path. ie. A pat is a means to get to a particular file or directory on the system. 

### Absolute & Relative Paths 

Either can be used to get to a file or directory.

File system in Linux is a *hierarchical* structure.

Atop the structure is the **root** directory. 
- denoted by a single slash
- has subdirectories and so on

***Absolute Paths*** specify a location (-/d) in relation to the root directory. Always begin with "/"

***Relative Paths*** specify a location (-/d) in relation to where we currently are in the system. These do NOT begin with a slash.

examples: 

`ls documents` is a relative path 
- displays contents of *current* directory's documents directory 


`ls /home/ryan/documents` is an absolute path 
- this could display contents of ryan's documents directory no matter if you're currently there or in another user's directory 

### More Paths 

- ~ (tilde) is a shortcut for your home directory 
    - if /home/ryan is your home directory, you could go to ryan's documents with the path 
    ```
    /home/ryan/documents 
    or 
    ~/documents
    ``` 
- . (dot) referene to your current directory 
- .. (dotdot) reference to the parent directory, can be used several times to keep going up the hierarchy

- cd [loacation] 
    - running cd without arguments will always take you back to your home directory 
    - argument can be used to move up/down hierarchy 

- Tab Completion 
    - after starting to type a path tab will auto complete, or hit tab again to show possibilities
