import subprocess, datetime, sys

def run(cmd, check=True, capture=False):
    return subprocess.run(
        cmd, shell=True, check=check,
        capture_output=capture, text=True
    )

def changed_files():
    r = run("git status --porcelain", check=False, capture=True)
    return r.stdout.strip()

ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
msg = f"Auto commit at {ts}"

print("Pulling remote (rebase)…")
run("git pull --rebase --autostash origin main", check=False)

if changed_files():
    print("Staging changes…")
    run("git add .")
    print("Committing…")
    run(f'git commit -m "{msg}"')
else:
    print("No changes to commit.")

print("Pushing to GitHub…")
run("git push", check=False)

print("✅ Done! Repository updated.")
