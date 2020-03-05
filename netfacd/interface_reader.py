#!/usr/bin/python3

import netifaces
print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n************** Details of Interface - ' + i + ' **************')
    try: ##This is a new line, you also need to indent the code below thisline by 4 whitespaces
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except: ##This is a new line
        print('Could not collect adapter information') ##Print and error msg


