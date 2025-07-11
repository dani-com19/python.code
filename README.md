git bash 
sage
😊
📝 Git Bash Commands with Descriptions
| **Command**                                        | **What It Does**                                                |
| -------------------------------------------------- | --------------------------------------------------------------- |
| `git --version`                                    | Check the installed version of git                             |
| `git config --global user.name "Your Name"`        | Set your Git username.                                          |
| `git config --global user.email "you@example.com"` | Set your Git email.                                             |
| `git init`                                         | Create a new Git repository in the current folder.              |
| `git clone <repo_url>`                             | Download (clone) a repository from GitHub to your computer.     |
| `git status`                                       | See which files have changed in your repo.                      |
| `git add <filename>`                               | Add a file to the staging area.                                 |
| `git add .`                                        | Add **all files** in the folder to staging.                     |
| `git commit -m "your message"`                     | Save (commit) your changes with a message.                      |
| `git push origin main`                             | Upload your commits to GitHub (to the `main` branch).           |
| `git pull origin main`                             | Download (pull) the latest changes from GitHub.                 |
| `git branch`                                       | See the list of branches in your repo.                          |
| `git branch <branch_name>`                         | Create a new branch.                                            |
| `git checkout <branch_name>`                       | Switch to another branch.                                       |
| `git merge <branch_name>`                          | Merge another branch into the one you’re on.                    |
| `git remote -v`                                    | Show the URLs of remote repositories connected to your project. |
| `git log`                                          | View commit history.                                            |
| `clear`                                            | Clears the Git Bash terminal screen.                            |
| `exit`                                             | Closes Git Bash.                                                |

✅ Here’s the typical flow to upload files to GitHub using Git Bash:

1 git init → Make the folder a Git repo.

2 git remote add origin <repo_url> → Link to your GitHub repo.

3 git add . → Stage all files.

4 git commit -m "First commit" → Save changes.

5 git branch -M main → Set branch to main.

6 git push -u origin main → Upload files to GitHub.


