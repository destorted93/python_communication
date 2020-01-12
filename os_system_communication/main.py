import os
import sys


# exec(open("extern_interface.py").read())

r = os.system("python extern_interface.py 1 2 3 4 5 6")

print("main script")

print(r)