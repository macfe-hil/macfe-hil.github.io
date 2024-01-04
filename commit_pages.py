import subprocess

def git_commit_with_user(message, username, email):
    try:
        # Set the Git user details
        subprocess.run(['git', 'config', 'user.name', username], check=True)
        subprocess.run(['git', 'config', 'user.email', email], check=True)

        # Run the git commit command
        subprocess.run(['git', 'pull'])
        subprocess.run(['git', 'add', '*'], check=True)
        subprocess.run(['git', 'commit', '-m', message], check=True)
        subprocess.run(['git', 'push'])

        print("Commit successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        # Handle the error, if needed

# Example usage
commit_message = "a0bdc0ee-b5df-fcb0-8d64-b8f858754f33"
git_username = "macformularacing"
git_email = "macformulaelectric@gmail.com"

git_commit_with_user(commit_message, git_username, git_email)
