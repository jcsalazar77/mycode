#!/usr/bin/python3

###########Explore Read##############
##create fileobject in "r"ead mode
configfile = open("/home/student/mycode/cfgread/vlanconfig.cfg", "r")

## display file to the screen - .read()
print(configfile.read())

## close file
configfile.close()

###########Explore Readlines########
## re-create file object to explore new method
configfile = open("/home/student/mycode/cfgread/vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

## interate through configlist
for x in configlist:
    print(x, end="")

## Always close your file
configfile.close()
