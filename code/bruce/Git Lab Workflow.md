# Git Lab Workflow

## The below is an example of workflow for creating branches for each new lab.

1. `git checkout main`
1. `git pull origin main`
1. `git checkout -b <new-branch-name>`
1. Do some code changes.
1. `git add -A`
1. `git commit -m <commit message>`
1. `git push origin <new-branch-name>`
1. Do some more code changes.
1. `git add -A`
1. `git commit -m <commit message>`
1. `git push origin <new-branch-name>`
1. When lab is completed, create pull request on GitHub.
1. Repeat process for new labs.

## Use the following to switch between multiple in-process lab branches.

1. Git `add` and `commit` changes to current branch:  
    1. `git add -A`
    1. `git commit -m <commit message>`
1. Checkout the branch we want to work on:  
    * `git checkout <a-branch-name>`
1. Do the code changes for this branch.
1. Git `add` and `commit` changes to the new current branch `<a-branch-name>`:  
    1. `git add -A`
    1. `git commit -m <commit message>`
1. Checkout some other branch we want to work on:  
    * `git checkout <some-other-branch-name>`
1. Repeat process as needed.
