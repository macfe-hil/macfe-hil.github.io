import subprocess
import git

def push_with_rebase(repo_path, branch_name):
    repo = git.Repo(repo_path)

    # Fetch updates from the remote repository
    repo.remotes.origin.fetch()

    # Ensure we are on the branch that needs to be updated
    repo.heads[branch_name].checkout()

    # Rebase changes
    repo.git.rebase('origin/' + branch_name)

    # Push the changes, forcing the update to the remote branch
    repo.git.push()

def configure_git_user_email(repo_path, git_username, git_email):
    repo = git.Repo(repo_path)

    # Set Git user name and email for the repository
    repo.config_writer().set_value("user", "name", git_username).release()
    repo.config_writer().set_value("user", "email", git_email).release()

def add_and_commit_changes(repo_path, commit_message):
    repo = git.Repo(repo_path)

    # Add all changes to the index
    repo.git.add('*')

    # Commit changes
    repo.index.commit(commit_message)

# Example usage
repo_path = "."
branch_name = "main"
commit_message = "3df1bf55-a9b6-a7f5-d7b6-0839cbeb8f70"
git_username = "macformularacing"
git_email = "macformulaelectric@gmail.com"

configure_git_user_email(repo_path=repo_path, git_username=git_username, git_email=git_email)
add_and_commit_changes(repo_path=repo_path, commit_message=commit_message)
push_with_rebase(repo_path=repo_path, branch_name=branch_name)