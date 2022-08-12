import subprocess
import os

# completed = subprocess.run(
#     "cd", shell=True, capture_output=True, text=True)

# completed = subprocess.run(
#     "python -u Testing//other.py", shell=True, capture_output=True, text=True)

# print("arg", completed.args)
# print("returncode", completed.returncode)
# print("stderr", completed.stderr)
# print("stdout", completed.stdout)

# subprocess.run("dir", shell=True)
try:
    completed = subprocess.run(
        "false", shell=True, capture_output=True, text=True, check=True)
    print("arg", completed.args)
    print("returncode", completed.returncode)
    print("stderr", completed.stderr)
    print("stdout", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)
