import os
import datetime
import random
import sys

# 🎲 Adjust this to control how often the bot commits
RUN_PROBABILITY = 0.5

# Randomly decide whether to commit this run
if random.random() > RUN_PROBABILITY:
    print("🎲 Skipping this run (decided not to commit).")
    sys.exit(0)

# Proceed with a commit
timestamp = datetime.datetime.utcnow().isoformat()
log_entry = f"{timestamp}: Daily automated commit\n"

# Write to log.txt 
with open("log.txt", "a") as f:
    f.write(log_entry)

print(f"✅ Writing to log.txt: {log_entry.strip()}")

# Git operations
os.system("git add log.txt")
os.system(f"git commit -m 'Automated daily commit at {timestamp}'")
os.system("git push origin main")

print("🚀 Commit pushed successfully.")
