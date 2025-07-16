import os
import datetime
import random
import time

n = random.randint(3, 9)
print(f"Making {n} commits...")

for i in range(n):
    timestamp = datetime.datetime.utcnow().isoformat()
    filename = f"commit_{timestamp.replace(':', '').replace('.', '')}.txt"

    with open(filename, "w") as f:
        f.write(f"Commit number {i+1} at {timestamp}\n")

    os.system(f"git add {filename}")
    os.system(f"git commit -m 'Automated commit {i+1} of {n}'")
    os.system("git push origin main")  # Push after each commit

    time.sleep(2)  # Optional: prevent push race conditions
