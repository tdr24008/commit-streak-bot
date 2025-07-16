import os
import random
import datetime
import time

n = random.randint(5, 10)
print(f"Making {n} commits...")

for i in range(n):
    timestamp = datetime.datetime.utcnow().isoformat()
    with open("log.txt", "a") as f:
        f.write(f"{timestamp}: Commit number {i+1}\n")

    os.system("git add .")
    os.system(f"git commit -m 'Automated commit {i+1} of {n}'")
    os.system("git push origin main")  # ✅ Push immediately after each commit
    time.sleep(2)  # optional: avoid hitting rate limits
