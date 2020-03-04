#!/usr/bin/python3

#open file in read mode
dnsfile = open("/home/student/mycode/fact/dnsservers.txt", "r")

#create list of lines
dnslist = dnsfile.readlines()

#loop over lines
for svr in dnslist:
    print(svr, end="")

#close your file
dnsfile.close()
