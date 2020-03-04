#!/usr/bin/python3
  
#open file in read mode
with open("/home/student/mycode/fact/dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # loop over lines
    for svr in dnsfile:
        svr = svr.rstrip('\n') # remove newline char if it exists
                               # would exist on all but last line
        #IF the sting svr ends with 'org'
        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
        # Else-IF the string svr ends with 'com'
        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")


# no need to close our file, it will be closed automatically
