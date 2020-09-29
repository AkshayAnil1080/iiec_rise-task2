#!/usr/bin/python3



print("content-type: text/html")
print()   # diff the header and the code below

import subprocess
x="pop"

y=subprocess.getoutput("sudo useradd youruser")
print("hello, youruser has been successfully created, check by 'id youruser'")
print(y)
