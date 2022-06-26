# Create A Lab Branch

## Notes and Assumptions
* The author is using PowerShell for their CLI so example interface may look different than the user's interface. But both the terminal commands (examples: `cd`, `ls`, `pwd`) and the git commands should work in most CLI interfaces.
* When some text below is placed between `<` and `>`, that means the user should provide their own text in the command and the user should not include the `<` and `>`.
    * Branch name form (in all lower-case):  
        * `studentname-labnumber-lab-name`
    * Example (for [Lab 0: Getting Started](https://github.com/PdxCodeGuild/class_062722/blob/main/0%20General/00%20Getting%20Started)):
        * studentname: `bruce`
        * labnumber: `lab00`
        * lab-name: `getting-started`
        * The branch name would be `bruce-lab00-getting-started`.

## Objectives

## Process

1. Open CLI

1. `cd` into repository (if not already there). We want to be in root of repository directory for this activity. But, in general, git commands can be executed in any directory within the repository:  

1. Check status of repository:  
    ```
    git status
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name> git status
        On branch main
        Your branch is up to date with 'origin/main'.

        nothing to commit, working tree clean
        PS C:\Users\Bruce\Programming\class_name>
        ```
    * NOTES:  
        * Regarding the `origin/main` in the output: `origin` is the local name for the associated remote repository. And `main` is the branch name on that repository.
        * The local branch `main` is 'up to date' with the branch `main` of remote repository named `origin`.

1. Checkout local `main` `branch`, if not already checked out:  
    ```
    git checkout main
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name> git checkout main
        Already on 'main'
        Your branch is up to date with 'origin/main'.
        PS C:\Users\Bruce\Programming\class_name>
        ```

1. `pull` recent commits of branch `main` of remote repository named `origin` to local `main` branch:  
    ```
    git pull origin main
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name> git pull origin main
        From https://github.com/brucestull/class_name
        * branch            main       -> FETCH_HEAD
        Already up to date.
        PS C:\Users\Bruce\Programming\class_name>
        ```

1. Create and checkout a local `branch` from local `main` for the lab:  
    ```
    git checkout -b <new-branch-name>
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name> git checkout -b bruce-lab00-getting-started
        Switched to a new branch 'bruce-lab00-getting-started'
        PS C:\Users\Bruce\Programming\class_name>
        ```

1. Push current branch `bruce-lab00-getting-started` to remote repository `origin`:  
    ```
    git push origin bruce-lab00-getting-started
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name> git push origin bruce-lab00-getting-started
        Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
        remote:
        remote: Create a pull request for 'bruce-lab00-getting-started' on GitHub by visiting:
        remote:      https://github.com/brucestull/class_name/pull/new/bruce-lab00-getting-started
        remote:
        To https://github.com/brucestull/class_name.git
        * [new branch]      bruce-lab00-getting-started -> bruce-lab00-getting-started
        PS C:\Users\Bruce\Programming\class_name>
        ```

1. Perform coding work on this branch. Verify current branch at any time by using:  
    ```
    git status
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name> git status
        On branch bruce-lab00-getting-started
        nothing to commit, working tree clean
        PS C:\Users\Bruce\Programming\class_name>
        ```

1. Frequently use the following while working on the code to push changes to the remote repository as work is performed:  
    1. `git add` (with any of the appropriate options below, or other options) the changes to the current commit.
        * `git add .`
            * Adds all changed directories and files in current directory.
        * `git add -A`
            * Adds all changed directories and files throughout the whole repository.
        * `git add <user-specific-file>`
            * Adds only the file specified by `<user-specific-file>`
    1. `git commit -m "<specific commit message>"`
    1. `git push <remote-repository-name> <local-branch-name>`

1. Create a pull request on GitHub when the lab is completed.

* Delete the branch after the lab has been graded and merged with the class'es `main` branch on remote repository on GitHub:  
    * Use the remote repository state to remove local references to remote repository:  
        ```
        git remote update origin --prune
        ```
    * Delete local branch:  
        ```
        git branch -d <branch-name-of-graded-lab>
        ```

* If there are several labs still in progress, use `git checkout` to switch between branches:  
    1. List current local branches:  
        ```
        git branch
        ```
        * Sample command and output (current branch is indicated by '*' next to branch name):  
            ```
            PS C:\Users\Bruce\Programming\class_name> git branch
              bruce-lab00-getting-started
            * bruce-lab01-doing-python
              main
            PS C:\Users\Bruce\Programming\class_name>
            ```
    1. `git checkout` the appropriate lab branch:  
        ```
        git checkout <specific-branch-name>
        ```
        * Sample command and output:  
            ```
            PS C:\Users\Bruce\Programming\class_name> git checkout bruce-lab00-getting-started
            Switched to branch 'bruce-lab00-getting-started'
            PS C:\Users\Bruce\Programming\class_name>
            ```



