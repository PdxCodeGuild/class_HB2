# Create A Lab Branch

## Notes and Assumptions
* The author is using PowerShell for their CLI so thier interface may look different than the user's interface. But both the terminal commands (examples: `cd`, `ls`, `pwd`) and the git commands should work in most CLI interfaces.
* When some text below is placed between `<` and `>`, that means the user should provide their own text in the command and the user should not include the `<` and `>`.
    * Example (for [Lab 0: Getting Started](https://github.com/PdxCodeGuild/class_062722/blob/main/0%20General/00%20Getting%20Started)):
        * studentname: `bruce`
        * labnumber: `lab00`
        * lab-name: `getting-started`
        * The branch would be `bruce-lab00-getting-started`.

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

1. Create and checkout a lab local `branch` from local `main`:  
    ```
    git checkout -b <new-branch-name>
    ```
    * Sample command and output:  
    ```

    ```

