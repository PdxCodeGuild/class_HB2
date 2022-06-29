# Git Lab Workflow

## The below is an example of workflow for creating branches for each new lab.

* Replace the `<new-branch-name>` items below with your appropriate formed `<studentdirectoryname-labnumber-lab-name>` branch name.
* An example `<new-branch-name>` would be `bruce-lab01-python-exercise`

1. Checkout the `main` branch since we want to keep it syncronized with remote:  
    `git checkout main`
1. Retrieve the remote changes to `main` branch and sync them to local repository:  
    `git pull origin main`
1. Create a new branch `<new-branch-name>` from current state of `main` branch:  
    `git checkout -b <new-branch-name>`
1. Do some code changes.
1. Add all the changes made to git tracking (or add only `<filename>` or `<directoryname>` changes):  
    `git add -A`
1. Commit the changes made to the branch:  
    `git commit -m <commit message>`
1. Push local changes to branch `<new-branch-name>` to the remote repository `origin`:  
    `git push origin <new-branch-name>`
1. Do some more code changes.
1. Add all the changes made to git tracking:  
    `git add -A`
1. Commit the changes made to the branch:  
    `git commit -m <commit message>`
1. Push local changes to branch `<new-branch-name>` to the remote repository `origin`:  
    `git push origin <new-branch-name>`
1. When lab is completed, [create pull request on GitHub](10%20GitHub%20Pull%20Request.md).
1. After lab has been graded and pull request approved, perform the following two commands to remove the reference to the remote branch, and then delete your local branch:  
    1. `git remote update origin --prune`
    1. `git branch -d <graded-and-merged-branch-name>`

1. Repeat process for new labs.

## Use the following to switch between multiple in-process lab branches.

1. Git `add` and `commit` changes to current branch:  
    1. `git add -A`
    1. `git commit -m <commit message>`
1. Checkout the different branch we want to work on:  
    * `git checkout <a-branch-name>`
1. Do the code changes for this branch.
1. Git `add` and `commit` changes to the new current branch `<a-branch-name>`:  
    1. `git add -A`
    1. `git commit -m <commit message>`
1. Checkout some other branch we want to work on:  
    * `git checkout <some-other-branch-name>`
1. Repeat process as needed.

## Use the following to delete branches for labs which have already been graded.
* NOTE: We delete the branches after they have been merged into `main` since the work has been completed and all the changes have been recorded in the `commit`s. We no longer need the branches.

1. Sync our local record of remote branches. This will remove local references to branches which have been deleted on remote:  
    * `git remote update origin --prune`
1. Delete the local copy of the branch:  
    * `git branch -d <lab-branch-which-has-been-graded>`
