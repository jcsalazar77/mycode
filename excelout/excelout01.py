#!/usr/bin/python3

import pyexcel

def get_ip_data():
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What is the driver associated with this device? ")
    input_device = input("What is the device type? ")
    input_mfg = input("Who is the Mfg.? ")
    d = {"IP": input_ip, "driver": input_driver, "device type": input_device, "Mfg.": input_mfg}
    return d

# Runtime
mylistdict = []

print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data()) # add an item to the list returned by get_ip_data() {"IP": value, "driver": value}
    keep_going = input("\nWould you like to add another value? Enter to continue, or enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

filename = input("\nWhat is the name of the *.xls file? ")
pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

print("The file " + filename + ".xls should be in your local directory")

