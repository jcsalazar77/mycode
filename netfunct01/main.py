#!/usr/bin/python3

# function to push commands
def commandpush(devicecmd): #devicecmd==list
    for coffeetime in devicecmd.keys():
        print('\nHandshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to the devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to send command --> ' + mycmds )
            #we'll learn to write code that sends cmds to device here

#start main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}
    print("Welcome to the network device command pusher") #welcome msg

    ##get data set
    print("\nData set found\n")

    ##run
    commandpush(work2do) #call function to push commands to devices

# Call our main function
main()

