import os
from random import randint
from datetime import datetime, timedelta
import subprocess

# Your GitHub username and PAT (replace with actual values)
GITHUB_USERNAME = 'ELKINANI-YOUNESS'
GITHUB_TOKEN = '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'  # Ensure this token is kept secret

# Set the remote URL with PAT for authentication
REMOTE_URL = f'https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/super-octo-bassoon.git'

# Update the remote origin URL with PAT
subprocess.run(['git', 'remote', 'set-url', 'origin', REMOTE_URL], check=True)

# Loop through the days
for i in range(1, 365):
    # Randomly determine how many commits to make on this day
    for j in range(randint(1, 10)):
        # Calculate the date for 'i' days ago
        d = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d %H:%M:%S')

        # Write to the file (optional, just for demonstration)
        with open('file.txt', 'a') as file:
            file.write(f'Commit on {d}\n')

        # Set the GIT_COMMITTER_DATE environment variable
        os.environ['GIT_COMMITTER_DATE'] = d
        os.environ['GIT_AUTHOR_DATE'] = d  # Make the author date match the committer date

        # Git commands with the specific date
        subprocess.run(['git', 'add', '.'], check=True)
        
        # Commit changes with the specific date
        commit_message = f"Commit for {d}"
        result = subprocess.run(['git', 'commit', '--date', d, '-m', commit_message], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Error committing: {result.stderr}")
            continue  # Skip to the next iteration if commit fails

    # Push the commits to the remote repository
    result = subprocess.run(['git', 'push', '-u', 'origin', 'main'], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error pushing to GitHub: {result.stderr}")
    else:
        print("Successfully pushed commits.")

print("Finished making commits.")
