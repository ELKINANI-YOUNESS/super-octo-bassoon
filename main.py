import os
from random import randint
from datetime import datetime, timedelta

# Your GitHub username and PAT (replace with actual values)
GITHUB_USERNAME = 'ELKINANI-YOUNESS'
GITHUB_TOKEN = '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'  # Ensure this token is kept secret

# Set the remote URL with PAT for authentication
REMOTE_URL = f'https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/super-octo-bassoon.git'

# Update the remote origin URL with PAT
os.system(f'git remote set-url origin {REMOTE_URL}')

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
        os.system('git add .')
        os.system(f'git commit --date="{d}" -m "Commit for {d}"')

    # Push the commits to the remote repository
    os.system('git push -u origin main')

print("Finished making commits.")
