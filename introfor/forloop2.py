#!/usr/bin/python3
  
#create list of strings
vendors = ["cisco", "juniper", "big ip", "f5", "arista", "alta3", "zach", "stewart"]

#create a second list of strings
approved_vendors = ["cisco", "juniper", "big ip"]


#loop across the list of strings
for x in vendors:
    print("\nThe vendor is " + x, end="") #new line, print current vendor, and end without new line
    if x not in approved_vendors: #if x does not appear in the list approved_vendors
        print(" - NOT AN APPROVED VENDOR!", end="")

print("\nOur loop has ended.") #when the loop ends, print this
