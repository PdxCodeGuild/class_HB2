# Git Clone a Repository

1. Obtain the url for the repository.
    * Example URL:
        * https://github.com/PdxCodeGuild/class_062722.git

1. Navigate to the directory you want to be the parent of the git repository directory.

1. Verify directory location:  
    ```
    pwd
    ```
    * Sample command and output:
        ```
        PS C:\Users\Bruce\Programming> pwd

        Path
        ----
        C:\Users\Bruce\Programming

        PS C:\Users\Bruce\Programming>
        ```

1. Clone the repository.
    * This command will generate a directory with the same name as the repository.
    ```
    git clone <repository-url>
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming> git clone https://github.com/PdxCodeGuild/class_062722.git class_062722
        Cloning into 'class_062722'...
        remote: Enumerating objects: 220, done.
        remote: Counting objects: 100% (138/138), done.
        remote: Compressing objects: 100% (99/99), done.
        Receiving objects: 100% (220/220), 114.59 KiB | 1.76 MiB/s, done.2

        Resolving deltas: 100% (67/67), done.
        PS C:\Users\Bruce\Programming>
        ```
    * You can, alternatively, use your own filename:
    ```
    git clone <repository-url> <repisitory-directory-name>
    ```

