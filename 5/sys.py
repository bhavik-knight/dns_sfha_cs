import sys
from pathlib import Path

print("Paths:=")
print("-" * 80)
# print path of the current directory
print(sys.path[0])

# other way of doing it using Path function from the pathlib
print(Path(__file__).parent)
print("-" * 80)
print()

print("Versions:=")
print("-" * 80)
# check the python version
print(sys.version)

# check the version info, which gives full info, major, minor, micro (major 3, minor 11, micro 4)
print(sys.version_info)
print("-" * 80)
print()

# printing on stdout/stderr
lines = ["This is the output 1", "This is output 2"]
errors = ["Error has occured!", "Something went wrong!"]

print("Print output + errors:=")
print("-" * 80)
sys.stdout.writelines(map(lambda line: line + "\n", lines))
sys.stderr.writelines(map(lambda error: error + "\n", errors))
print("-" * 80)
print()

sys.stdout = open("out.log", "w")
sys.stderr = open("err.log", "w")

# this usually writes on console if file is not open
# so if you comment line above two lines it won't generate file, but print on console
sys.stdout.writelines(map(lambda line: line + "\n", lines))
sys.stderr.writelines(map(lambda error: error + "\n", errors))
