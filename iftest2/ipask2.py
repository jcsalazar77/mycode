#!/usr/bin/python3

ipchk = input("Apply an IP address: ")

if ipchk == "192.168.70.1":
    print("Looks like the IP address of the gateway was set to " + ipchk + " This is not recommended")
elif ipchk:
    print("Looks like the IP address was set: " + ipchk)
else:
    print("You did not provide an IP address")

