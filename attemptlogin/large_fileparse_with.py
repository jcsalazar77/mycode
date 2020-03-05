#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 #counter for failures

#open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    # loop over the file
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = 1

print("The number of failed login attempts is", loginfail)

