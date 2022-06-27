# Git Clone a Repository

1. Obtain the url for the repository.
    * Example URL:
        * https://github.com/PdxCodeGuild/class_name.git

1. Navigate to the directory you want to be the parent of the git repository directory.
    * I choose a directory named "Programming' which is just inside my home directory.
        * C:\Users\Bruce\Programming

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

1. Clone the repository:  
    * This command will generate a directory with the same name as the repository:  
    ```
    git clone <repository-url>
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming> git clone https://github.com/PdxCodeGuild/class_name.git
        Cloning into 'class_name'...
        remote: Enumerating objects: 224, done.
        remote: Counting objects: 100% (142/142), done.
        remote: Compressing objects: 100% (102/102), done.
        Receiving objects:  58% (130/224)sed 89 (delta 27), pack-reused 82
        Receiving objects: 100% (224/224), 115.51 KiB | 1.72 MiB/s, done.
        Resolving deltas: 100% (68/68), done.
        PS C:\Users\Bruce\Programming>
        ```
    * You can, alternatively, use your own directory name:  
        ```
        git clone <repository-url> <repository-directory-name>
        ```

1. Change directory into the repository and investigate the contents:  
    ```
        cd <directory-name>
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming> cd .\class_name\
        PS C:\Users\Bruce\Programming\class_name>
        ```

1. Show file contents:  
    ```
    ls
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name> ls

            Directory: C:\Users\Bruce\Programming\class_name

        Mode                 LastWriteTime         Length Name
        ----                 -------------         ------ ----
        d----          2022-06-27    16:16                0 General
        d----          2022-06-27    16:16                1 Python
        d----          2022-06-27    16:16                code
        -a---          2022-06-27    16:16           8198 README.md

        PS C:\Users\Bruce\Programming\class_name>
        ```

1. Show directory contents, including hidden directories and files:  
    ```
    dir -Force
    ```
    * Sample command and output:  
        ```
        PS C:\Users\Bruce\Programming\class_name> dir -Force

            Directory: C:\Users\Bruce\Programming\class_name

        Mode                 LastWriteTime         Length Name
        ----                 -------------         ------ ----
        d--h-          2022-06-27    16:20                .git
        d----          2022-06-27    16:16                0 General
        d----          2022-06-27    16:16                1 Python
        d----          2022-06-27    16:16                code
        -a---          2022-06-27    16:16           8198 README.md

        PS C:\Users\Bruce\Programming\class_name>
        ```