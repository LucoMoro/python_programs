import subprocess

completed = subprocess.run(["python", "other.py"], capture_output=True, text=True)
print("args", completed.args)
print("returncode", completed.returncode)
#print("stderr", completed.stderr)
print("stdout", completed.stdout)