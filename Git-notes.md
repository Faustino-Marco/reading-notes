# Git Intro

### Quick notes from lecture

git add - stages your changes -- gets it ready for its snapshot
git commit - saves the changes - ner version! --takes the snapshot
git push - pushes changes to github --sends the snapshot to the cloud/remote

what is local? --YOUR computer

git pull --pulls all the changes from github/cloud/remote

## Reading Notes 

For reference, here's the Git Intro [Article](https://blog.udemy.com/git-tutorial-a-comprehensive-guide/).


### Version Control

- Programmers used to use a *local* VCS on a hard disk.

- *Centralized* Version Control came about when innovators sought to solve the problem of collaborative development.
    - this was done on a single serve storing all changes and file versions.

- *Distributed* Version Control
    - solves major vulnerability of the CVS: server as single point of failure. 
        - If the server goes down no one can work on dev.
        - If the server is corrupted with the abscence of backups, all work is lost except for what's on local machines.
    - DVCS allows for multiple "mirrored repositories"

## Git

### What is git?

- Snapshots 
    - every time you save a changed version of your project (called a 'commit'), Git creates a *snapshot* of the file and stores a reference to it.
- Local Operations
    - Git mostly relies on local operations
    - this way a project's history resides on the local disk, which eliminates the need to fetch history info from server.
        - This allows one to work on a project offline or without a VPN
- Tracking Changes
    - ALL changes are tracked by Git
    - Git will always detect file corruption or loss of information in transit
- Loss of Data
    - git makes it difficult for a snapshot to be lost.
- Git States
    - Files in Git can reside in 3 main states
        - Committed
        - Modified
        - Staged 

![Git Flowchart](https://blog.udemy.com/wp-content/uploads/2015/08/image066-768x618.png) 


- History of Git
    - Rooted in open source software project Linux kernel.
    - Devs began using a DVCS called BitKeeper in '02.
    - Linus Torvalds (chief architect of Linux kernel) began creating Git because of conflict between DVCS and Linux kernel
    - Since inception in '05, Git has become one of the most utilized VCS's worldwide.

- Get started
    - three ways to install
        - install as a package
        - install via another installer
        - Download and compile the source code

#### Mac OS X

Terminal
The simplest method for installing Git on a Mac (for Mavericks 10.9 and above) is running Git from the Terminal. If Git is not installed, you will see a prompt for installation. 

Git Website

You can also download Git by visiting this link and following the posted directions:

http://git-scm.com/download/mac

GitHub

A third option is to install Git as part of the GitHub for Mac install. GitHub is repository hosting service, which we will discuss in a future section.

Download GitHub for Mac via the following link:

http://mac.github.com


#### Windows 

Git Website

You can download Git by visiting this link and following the posted directions:

http://git-scm.com/download/win

GitHub

Install Git as part of the GitHub for Windows install.

http://windows.github.com

#### Linux 

Package Manager

You can try installing Git via your distribution’s inherent package management tool.

For Fedora:

$ sudo yum install git
For Ubuntu:

$ sudo apt-get install git
Git Website

To download Git for Linux, visit this link and follow the posted directions:

http://git-scm.com/download/linux 

The rest of the page can be found [here](https://blog.udemy.com/git-tutorial-a-comprehensive-guide/).