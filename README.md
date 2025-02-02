**This File contains the set of useful git commands in the workspace**
git clone https://github.com/your-username/repository-name.git  --->  To clone the Repository using URL
cd repository-name  --> Navigate to that repo
mkdir new-folder-name  --> to create a new folder
echo > example.py --> creates a example.py file  (echo example.py -> It will just print the text example.py to the terminal, but it won't create a file.)
git pull origin main --rebase   --> to fetch and merge remote changes, to resolve conflicts in local branch (NEED to run before pushing ONLY if any changes to repo)
git add example.py   --> to add specific file
git commit -m "Fixed bug in example.py"  --> to commit changes
git push origin main  --> to push into repo in main branch
git push origin main --force  --> to overwrite the remote branch with your local changes(Be careful on data loss)
git add folder-name  --> to add a folder
git commit -m "Added my-folder with new files"  --> to commit changes
git push origin main  --> to push the folder and all its files into Git
