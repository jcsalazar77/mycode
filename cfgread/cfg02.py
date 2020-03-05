#!/usr/bin/python3

##create file object in read mode
configfile = open("/home/student/mycode/cfgread/vlanconfig.cfg", "r")

## display file to the screen
configblog = configfile.read()

##break configblog across line boundaries (strips out /n)
configlist = configblog.splitlines()

## display list with no "\n"
print(configlist)

## Always close your file
configfile.close()

