# Removing and ignoring .DS_Store

A Mac computer is creating a so called .DS_Store file in every folder for metadata storage. Although this is a useful feature usually you do not want it to be stored in a git repository. Git newbies tend to not take care of it but the more you interact with such repos it's getting a real pain. You can avoid that behaviour by doing the following:

## Removing an accidentially .DS-Store file from repository

1. Open the Terminal app
2. Open (clone / pull) the repository from origin source (e.g. GitHub)
3. Change to the directory of the local repository clone
4. Type 'find . -name .DS_Store -print0 | xargs -0 git rm --ignore-unmatch'
5. Add changes, commit and push to remote repository

## Preventing .DS_Store from beeing included to any repository

1. Check for git config directory in ~/.config (should be 'git')
2. If there is no git dir create one with 'mkdir ~/.config/git'
3. Create a git ignore file and enter the ignore rule to this file 'echo .DS_Store >> ~/.config/git/ignore'

Happy using git! :)