import os
import random
import datetime
import subprocess

# Generate 1 to 5 commits
num_commits = random.randint(5, 10)

for i in range(num_commits):
    # Write to a dummy file
    with open("log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}: Commit number {i+1}\n")

    # Git commands
    subprocess.run(["git", "add", "log.txt"])
    subprocess.run(["git", "commit", "-m", f"Automated commit {i+1} of {num_commits}"])
