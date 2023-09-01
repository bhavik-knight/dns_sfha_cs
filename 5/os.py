import os
import subprocess
import sys
from pathlib import Path

print("Some basic os commands:=")
print("-" * 80)
# current working dir
print("Current directory", os.getcwd())

# process id
print("Current process id", os.getpid())

# operating system
print("Current os name", os.name)

# details name
print("Detailed os name", os.uname())

# platform
print("System platform", sys.platform)
print("-" * 80)


print("\nWalking through each file and directory in the current folder:=")
print("-" * 80)
# current path
current_path = Path(__file__).parent

# dir name
new_dir = "os_output"

# try to run a subprocess to create dir
# one way to create directory using subprocess
# not recommended way to create dir
# if subprocess.run(["mkdir", new_dir]).returncode:
#     print(f"Directory: {new_dir} already exists.")

# make directory
try:
    os.mkdir(f"{current_path.joinpath(new_dir)}")
except FileExistsError:
    pass

# creating a path for the output file
output_path = current_path.joinpath("os_output/output.txt")

# walk thourgh file-dir-tree in the current dir "."
# takes topdown argument value is True | False
for path, dirs, files in os.walk(".", topdown=False):
    with open(output_path, "w") as f:
        for name in files:
            f.write(f"file: {current_path.joinpath(name)}\n")

        for name in dirs:
            f.write(f"dir: {current_path.joinpath(name)}\n")

print(
    f"See all the files and directory in the current folder in this file: {output_path}"
)
print("-" * 80)


# creating subprocess to check ping of user input website
print("\nSubprocess:=")
print("-" * 80)
website = str.strip(input("Please give me a website link to check ping: "))
if subprocess.run(["ping", "-c", "4", website]).returncode:
    print("Something went wrong!")
else:
    print("Process run successfully!")
print("-" * 80)
