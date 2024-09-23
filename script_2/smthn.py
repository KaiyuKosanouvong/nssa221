#!/usr/bin/python3
# Kaiyu Kosanouvong / NSSA221 - Script 2
# runs a diagnostic on the host system covering various specifications

# import os and netifaces
# to get netifaces:
# pip install netifaces
import os
import netifaces

# returns IP address of system
def returnIP():
    # get ip
    ip = os.popen("ip r |grep '^default' |awk '{print $9}'").read().strip("\n")

    return ip

# return net IP address
def returnNetIP():
    netIP = os.popen("ip r |awk '{print $1}'").read().strip("\n").split("\n")[1]
    return netIP

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

def main():
    # clear terminal 
    os.system("clear")
    # run logistics
    print("----- System Logistics -----\n"
          + "IPv4 Address: " + returnIP() + "\n"
          + "Net IP: " + returnNetIP() + "\n"
          + "Default Gateway: " + defaultGate() + "\n")
    
if __name__ == '__main__':
    main()