# Lab 00: Getting Started

## Create Our Own Folder for Our Labs

* The sample code output provided here is using PowerShell, your output may be slightly different.

* For our very first lab we will be creating a folder to hold all of our labs. This will also be an exercise in utilizing git.

* NOTE: When some text below is placed between `<` and `>`, that means the user should provide their own text in the command and the user should not include the `<` and `>`.


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

1. Verify we are in a directory that is a git repository:  
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
1. Once we are inside the local repository (class_name folder) we can go ahead and create a new branch to store all of our changes for the current lab. Let's create a branch with our name followed by lab00 followed by lab name (studentname-labnumber-lab-name).
    * Example (for [Lab 0: Getting Started](https://github.com/PdxCodeGuild/class_062722/blob/main/0%20General/00%20Getting%20Started)):
        * studentname: `bruce`
        * labnumber: `lab00`
        * lab-name: `getting-started`
        * My name is 'Bruce' so my branch name would be `bruce-lab00-getting-started`.
    * The command we will use (where `<branch-name>` is replaced by your branch name decided above):  
        * This command creates a new branch named `<branch-name>` from the current state of the `main` branch.
            ```
            git checkout -b <branch-name>
            ```
            * Sample command and output:  
                ```
                PS C:\Users\Bruce\Programming\class_name> git checkout -b bruce-lab00-getting-started
                Switched to a new branch 'bruce-lab00-getting-started'
                PS C:\Users\Bruce\Programming\class_name>
                ```

1. We can verify current git branch and list local branches using `git branch`:  
    ```
    git branch
    ```
    * Current branch is indicated by the '*' in front of the branch name.
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name> git branch
        * bruce-lab00-getting-started
          main
        PS C:\Users\Bruce\Programming\class_name>
        ```

1. Verify contents of current directory:  
    ```
    ls
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name> ls

            Directory: C:\Users\Bruce\Programming\class_name

        Mode                 LastWriteTime         Length Name
        ----                 -------------         ------ ----
        d----          2022-06-27    03:50                0 General
        d----          2022-06-27    03:50                1 Python
        d----          2022-06-27    04:09                code
        -a---          2022-06-27    03:50           8198 README.md

        PS C:\Users\Bruce\Programming\class_name>
        ```
1. Change directory (folder) into the `code` directory:  
    ```
    cd code
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name> cd code
        PS C:\Users\Bruce\Programming\class_name\code>
        ```

1. Verify we are in `code` directory:  
    ```
    pwd
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name\code> pwd

        Path
        ----
        C:\Users\Bruce\Programming\class_name\code

        PS C:\Users\Bruce\Programming\class_name\code>
        ```

1. Create your directory inside the `code` directory. Use the lowercase version or your name:  
    ```
    mkdir <studentdirectoryname>
    ```
    * Sample command and output:  
        * My name is 'Bruce' so my directory will be `bruce`:  
        ```
        PS C:\Users\Bruce\Programming\class_name\code> mkdir bruce

            Directory: C:\Users\Bruce\Programming\class_name\code

        Mode                 LastWriteTime         Length Name
        ----                 -------------         ------ ----
        d----          2022-06-27    04:12                bruce

        PS C:\Users\Bruce\Programming\class_name\code>
        ```

1. Change directory into your personal directory:  
    ```
    cd <studentdirectoryname>
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name\code> cd bruce
        PS C:\Users\Bruce\Programming\class_name\code\bruce>
        ```

1. Inside your newly created personal directory (folder), create a `README.md` file.
    * This is a markdown file and is generally used to provide context to folders within Github.
    * This markdown file named `README.md` will hold your name, your directory name, and your GitHub username.
    * You can also add any other information or links to the file later if you choose.
    * The '#' below will make that line render as a heading in the markdown file.
    * We will use something like this, where `Firstname Lastname` is replaced by your first and last name:  
        ```
        echo "# Firstname Lastname" > README.md
        ```
        * Sample command and output:    
            ```
            PS C:\Users\Bruce\Programming\class_name\code\bruce> echo "# Bruce Stull" > README.md
            PS C:\Users\Bruce\Programming\class_name\code\bruce>
            ```

1. Open the `README.md` file in VS Code or other text editor.

1. Add directory name and GitHub username information to `README.md` and save the file:  
    * Sample `README.md` contents:  
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
        ```
        PS C:\Users\Bruce\Programming\class_name\code\bruce> git status
        On branch bruce-lab00-getting-started
        Untracked files:
        (use "git add <file>..." to include in what will be committed)
                ./

        nothing added to commit but untracked files present (use "git add" to track)
        PS C:\Users\Bruce\Programming\class_name\code\bruce>
        ```

1. Let's now add the files and directories we created to be tracked by git:  
    ```
    git add -A
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name\code\bruce> git add -A
        PS C:\Users\Bruce\Programming\class_name\code\bruce>
        ```
    * We used `git add -A` above to add all changed files to git tracking but we can add specific files or directories to tracking by the following two examples:
        * To add specific files to git tracking:  
            ```
            git add <filename>
            ```
        * To add specific directory to git tracking:  
            ```
            git add <directoryname>
            ```

1. Let's use `git status` again to verify we are tracking the proper files:  
    ```
    git status
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name\code\bruce> git status
        On branch bruce-lab00-getting-started
        Changes to be committed:
        (use "git restore --staged <file>..." to unstage)
                new file:   README.md

        PS C:\Users\Bruce\Programming\class_name\code\bruce>
        ```

1. We can now `commit` our changes to the branch `<studentname-labnumber-lab-name>` git history.
    * The `<commit message>` below is used to describe the changes this commit includes.
    * The `<commit message>` may be something like "Added directory for storing labs and included personal README.md"
    * We will use the command `git commit -m "<commit message>"`:  
        ```
        git commit -m "<commit message>"
        ```
        * Sample command and output:  
            ```
            PS C:\Users\Bruce\Programming\class_name\code\bruce> git commit -m "Added directory for storing labs and included personal README.md"
            [bruce-lab00-getting-started 80b110a] Added directory for storing labs and included personal README.md
            1 file changed, 7 insertions(+)
            create mode 100644 code/bruce/README.md
            PS C:\Users\Bruce\Programming\class_name\code\bruce>
            ```

1. Finally we can push our code to remote repository hosted on Github. This will allow the instructor and TAs to see the code changes and grade the labs:  
    ```
    git push origin <branch-name>
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name\code\bruce> git push origin bruce-lab00-getting-started
        Enumerating objects: 7, done.
        Counting objects: 100% (7/7), done.
        Delta compression using up to 8 threads
        Compressing objects: 100% (4/4), done.
        Writing objects: 100% (5/5), 481 bytes | 481.00 KiB/s, done.
        Total 5 (delta 1), reused 0 (delta 0), pack-reused 0
        remote: Resolving deltas: 100% (1/1), completed with 1 local object.
        remote:
        remote: Create a pull request for 'bruce-lab00-getting-started' on GitHub by visiting:
        remote:      https://github.com/PdxCodeGuild/class_062722/pull/new/bruce-lab00-getting-started
        remote:
        To https://github.com/PdxCodeGuild/class_062722.git
         * [new branch]      bruce-lab00-getting-started -> bruce-lab00-getting-started
        PS C:\Users\Bruce\Programming\class_name\code\bruce>
        ```

1. Create pull request on GitHub.
   * [GitHub Pull Request]()
