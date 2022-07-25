# Command Line Prep Readings

## [The Command Line](https://ryanstutorials.net/linuxtutorial/commandline.php) 
- Linux UI
- Text based interface to the system
- Typically issuing commands in CL
  - prompts and commands
- Bash
  - Bourne Again Shell
  - echo $SHELL displays current shell
- up and down arrow keys for command history

## [Basic Navigation](https://ryanstutorials.net/linuxtutorial/navigation.php)
- Where are we?
  - pwd
- What's in here?
  - ls
- abs / relative paths
  - absolute paths start with /
- home, current, parent directories
  - ~, ., ..
- change directory
  - cd

## [More About Files](https://ryanstutorials.net/linuxtutorial/aboutfiles.php)
  - everything is a file
    - some read only, some write only
  - linux is an extension-less system
    - no .exe, .txt, .png
    - linux doesn't care what the ext is 
  - linux is case sensitive
  - no spaces
  - escape with \
  - hidden files/dirs start with .

## [Manual Pages](https://ryanstutorials.net/linuxtutorial/manual.php)
- set of pages that explain every command available on your system including what they do, the specifics of how you run them and what command line arguments they accept.
- `man <command to look up>`
- Searching
  - `man -k <search term>`

## [File Manipulation](https://ryanstutorials.net/linuxtutorial/filemanipulation.php)
- `mkdir [options] <directory>`
  - creates directories
- `rmdir [options] <directory>`
  - removes directories
- touch creates 
- `cp [options] <source> <destination>`
  - copy and paste target from source into destination
- `mv [options] <source> <destination>`
  - move file alltogether
- `mv [options] <source> <source>`
  - changes name
- `rm/rmdir` remove empty files/dirs
  - `rm -r` gets rid of file and contents
## [Cheat Sheet](https://ryanstutorials.net/linuxtutorial/cheatsheet.php)

- I finally got to solidify the concepts of file manipulation, which I'd been lacking on up until this point. It seems pretty straightforward considering that theres usually a similar pattern/syntax with many commands.
- This also helped me remember that -k is the search option.