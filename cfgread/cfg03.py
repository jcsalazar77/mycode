#!/usr/bin/python3

## create file object in read mode
with open("/home/student/mycode/cfgread/vlanconfig.cfg", "r")as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto-closed

## display list with no "\n"
print(configlist)
