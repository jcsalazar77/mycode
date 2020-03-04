#!/usr/bin/python3
  
#open file in read mode
with open("/home/student/mycode/fact/dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # loop over lines
    for svr in dnsfile:
        # print and end without a newline
        print(svr, end="")

# no need to close our file, it will be closed automatically
