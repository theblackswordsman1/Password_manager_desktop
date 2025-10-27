import subprocess
import datetime

def run(cmd):
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Command failed: {cmd}")
        exit(1)

# Commit message with timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_message = f"Auto commit at {timestamp}"

print("Staging all changes...")
run("git add .")

print("Committing...")
run(f'git commit -m "{commit_message}"')

print("Pushing to GitHub...")
run("git push")

print("Done! Repository updated.")