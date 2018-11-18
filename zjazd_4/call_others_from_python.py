import os

x = os.system("ipconfing")
print(x)

# x = os.popen("ipconfing").read()
# print(x)

import subprocess

p = subprocess.Popen("notepad.exe")
print("lalaal")