#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi


pyttsx3.speak("hello how can i help you")

form=cgi.FieldStorage()


#osname = input("enter ur os name ; ")  # input works in terminal only. so html page i req
osname = form.getvalue("x")
osimage = form.getvalue("i")
        

print(osname)
cmd = "sudo docker run -d -i -t --name {0} {1}".format(osname,osimage)


output= sp.getstatusoutput(cmd)
status=output[0]
out=output[1]

print(status)
print(out)


if status == 0:
 print("os lauched {}.. ".format(osname))
else: 
 print("some error : {}".format(out))
