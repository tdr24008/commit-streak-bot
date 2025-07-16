import os
import datetime

# Generate a timestamp
timestamp = datetime.datetime.utcnow().isoformat()

# Append a log entry to a persistent file
with open("log.txt", "a") as f:
    f.write(f"{timestamp}: Daily automated commit\n")

# Stage and commit the change
os.system("git add log.txt")
os.system("git commit -m 'Automated daily commit at {timestamp}'")
os.system("git push origin main")  # Push the commit
