#!:/usr/bin/python3
# Kaiyu Kosanouvong / NSSA221 - Script 1
# runs a command line interface that performs a variety of network functions

# import os and netifaces
# to get netifaces:
# pip install netifaces
import os
import netifaces

# returns the default gateway of the system
def defaultGate():
    # Week 3 Scripting Review Code (Slide 19)
    try:
        # get gateway via netifaces
        gws = netifaces.gateways()
        def_GW = gws['default'][netifaces.AF_INET][0]
    except: # can also get gateway via os in case netifaces fails
        def_GW = os.popen("ip r |grep '^default' |awk '{print $3}'").read().strip("\n")

    return def_GW

# tests the local connection and returns results
def localConnect():
    # get local IP (default gateway)
    local_IP = defaultGate()

    # get ping test results
    pingtest = os.popen("ping -c 2 " + local_IP).read().strip("\n")
    return pingtest
    

# test remote connection and returns results
def remoteConnect():
    # get remote IP (RIT server)
    remote_IP = "129.21.3.17"

    # get ping test results 
    pingtest = os.popen("ping -c 2 " + remote_IP).read().strip("\n")
    return pingtest

# tests the dns resolution and returns results
def dnsResolution():
    # get DNS IP (RIT server)
    DNS_IP = "8.8.8.8"

    # get ping test results 
    pingtest = os.popen("ping -c 2 " + DNS_IP).read().strip("\n")
    return pingtest

# sets up a command line menu for the user
def menu():
    # while loop until user exits program
    while True:
        # parse for user input
        userInput = input("Please enter a command: \n" +
                        "(1) to get default gateway\n" +
                        "(2) to test local connection\n" +
                        "(3) to test remote connection\n" +
                        "(4) to test DNS resolution\n" +
                        "(5) to exit the program\n" +
                        "")
        
        if userInput == "1": # returns default gateway 
            def_GW = defaultGate()
            print("Your default gateway: " + def_GW + "\n")
        elif userInput == "2": # runs local connection test
            pingTest = localConnect()
            print("Local Test results: " + pingTest)
        elif userInput == "3": # runs remote connection test
            pingTest = remoteConnect()
            print("Remote Test results: " + pingTest)
        elif userInput == "4": # runs dns resolution test
            pingTest = dnsResolution()
            print("DNS Test results: " + pingTest)
        elif userInput == "5": # exits program
            print("bye!")
            exit()
        else: # invalid command case
            print("invalid command!\n")

def main():
    # clear terminal 
    os.system("clear")
    # run menu until exit is run
    menu()

if __name__ == '__main__':
    main()