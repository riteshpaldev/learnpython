12. How will you create a git repository?
Have git installed in your system. 
Then in order to create a git repository, create a folder for the project and then run git init. 
Doing this will create a .git file in the project folder which indicates that the repository has been created.
13. Tell me something about git stash?
Git stash can be used in cases where we need to switch in between branches and at the same time not wanting to lose edits in the current branch. Running the git stash command basically pushes the current working directory state and index to the stack for future use and thereby providing a clean working directory for other tasks.

14. What is the command used to delete a branch?
To delete a branch we can simply use the command git branch –d [head].
To delete a branch locally, we can simply run the command: git branch -d <local_branch_name>
To delete a branch remotely, run the command: git push origin --delete <remote_branch_name>
Deleting a branching scenario occurs for multiple reasons. One such reason is to get rid of the feature branches once it has been merged into the development branch.
15. What differentiates between the commands git remote and git clone?
git remote command creates an entry in  git config that specifies a name for a particular URL. Whereas git clone creates a new git repository by copying an existing one located at the URL.

16. What does git stash apply command do?
git stash apply command is used for bringing the works back to the working directory from the stack where the changes were stashed using git stash command.
This helps the developers to resume their work where they had last left their work before switching to other branches2::::1.
