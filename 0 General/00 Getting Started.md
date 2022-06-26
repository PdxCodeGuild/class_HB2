# Lab 00: Getting Started

## Create Our Own Folder for Our Labs

* For our very first lab we will be creating a folder to hold all of our labs. This will also be an exercise in utilizing git.

1. Open CLI.

1. Make sure we are in correct folder (directory). We should be inside <class_name> folder (directory). `pwd` shows the current 'working directory':  
    ```
    pwd
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name> pwd

        Path
        ----
        C:\Users\Bruce\Programming\class_name

        PS C:\Users\Bruce\Programming\class_name>
        ```

1. Once we are inside the repository (class_kiwi folder) we can go ahead and create a new branch to store all of our changes. Let's create a branch with our name followed by lab00 followed by lab name (studentname-labnumber-lab-name).
    * When some text below is placed between `<` and `>`, that means the user should provide their own text in the command and the user should not include the `<` and `>`.
        * Example (for [Lab 0: Getting Started](https://github.com/PdxCodeGuild/class_062722/blob/main/0%20General/00%20Getting%20Started)):
            * studentname: `bruce`
            * labnumber: `lab00`
            * lab-name: `getting-started`
        * My name is 'Bruce' so branch name will be `bruce-lab00-getting-started`.
    * The command we will use:  
        ```
        git checkout -b <branch-name>
        ```
        * Sample command and output:  
            ```
            git checkout -b bruce-lab00-getting-started
            ```

1. We can verify current git branch and list local branches using `git branch`:  
    ```
    git branch
    ```
    * Sample command and output:  
        ```

        ```

1. Change directory (folder) into the `code` directory:  
    ```
    cd code
    ```
    * Sample command and output:  

1. Verify we are in `code` directory:  
    ```
    pwd
    ```
    * Sample command and output:  

1. Create your directory inside the `code` directory. Use the lowercase version or your name. My name is 'Bruce' so my directory will be `bruce`:  
    ```
    mkdir bruce
    ```
    * Sample command and output:  

1. Change directory into your personal directory:  
    ```
    cd bruce
    ```
    * Sample command and output:  

1. Inside your newly created folder, create a `README.md` file. This is a markdown file and is generally used to provide context to folders within Github. This markdown file named `README.md` will hold your name, your directory name, and your GitHub username. You can also add any other information or links to the file later if you choose:  
    ```
    echo "# Bruce Stull" > README.md
    ```

1. Open the `README.md` file in VS Code or other text editor.

1. Add directory name and GitHub username information to `README.md` and save the file:  
    * Sample contents:  
        ```
        # Bruce Stull

        Directory Name:
        bruce

        GitHub Username:
        brucestull
        ```

1. Use `git status` to get the status of our branch:  
    ```
    git status
    ```
    * Sample command and output:  


1. Let's now add the files and directories we created to be tracked by git:  
    ```
    git add -A
    ```
    * Sample command and output:  
        ```

        ```
    * We used `git add -A` above to add all changed files to git tracking but we can add specific files or directories to tracking by the following two examples:
        * example 1
        * example 2

1. Let's use `git status` again to verify we are tracking the proper files:  
    ```

    ```
    * Sample command and output:  
        ```

        ```

1. We can now `commit` our changes to the branch's (`bruce-lab00-getting-started`) git history.
    * The <commit message> below is used to describe the changes this commit includes.
    * The <commit message> may be something like "Added directory for storing labs and included personal README.md"
    * We will use the command `git commit -m "<commit message>"`:  
    ```
    git commit -m "<commit message>"
    ```
    * Sample command and output:  
        ```

        ```

1. Finally we can push our code to remote repository hosted on Github. This will allow the instructors to see and code changes and grade labs:  
    ```
    git push origin main
    ```


