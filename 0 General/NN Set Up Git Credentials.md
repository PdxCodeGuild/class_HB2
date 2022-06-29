# Set Up Git Credentials

* We need to set up our local `git` installation to use the proper GitHub credentials when we `push` our branch changes to the remote repository. This document provides procedure to do do that setup.

## References:
* [Git - in 0 General directory](03%20Git.md)
* [Set up Git](https://docs.github.com/en/get-started/quickstart/set-up-git)
* [Caching your GitHub credentials in Git](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git)
* [Setting your username in Git](https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git#setting-your-git-username-for-every-repository-on-your-computer)
* [Setting your commit email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)

## Process:

1. Install `git`. Get the download here:
    * https://git-scm.com/downloads
        * TODO: Need to address the "default editor" option. Need to have a default editor already installed.
            * Git 2.37.0 Uses 'Git Credential Manager' if the option is selected.
            * get 'noreply' email from GitHub.
            * Git credential:
                * Uses:
                    * "Sign in with your browser"
                    * "Sign in with a code"
                    * Browser window stays blank after authentication.

1. Verify `git` is installed.
    * Execute the following command:
        ```
        git
        ```

1. Set your GitHub credentials for the entire computer (all repositories on your computer). **Execute the following command**:
    1. This `user.name` doesn't have to exactly match your GitHub username. **Execute the following command**:
        * `git config --global user.name "Your Name"`
    1. This `user.email` has to exactly match the email address you use for GitHub. **Execute the following command**:
        * `git config --global user.email you@email.com`
    1. This command sets up the `credential.helper` which provides authentication of your GitHub interactions on CLI with the GitHub repository. **Execute the following command**:
        * `git config --global credential.helper store`