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