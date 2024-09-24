#!/usr/bin/python3
# Kaiyu Kosanouvong / NSSA221 - Script 2
# runs a diagnostic on the host system covering various specifications

# import os and netifaces
# to get netifaces:
# pip install netifaces
import os
import netifaces

# DEVICE INFO
# returns the device information of the system: Hostname, Domain
def returnDevice():
    return (os.popen("hostname").read().strip("\n").split("."))


# NET INFO

# returns IP address of system
def returnIP():
    # get ip
    ip = os.popen("ip r |grep '^default' |awk '{print $9}'").read().strip("\n")

    return ip

# return network mask
def returnNetMask():
    netMask = os.popen("ip r |awk '{print $1}'").read().strip("\n").split("\n")[1]
    return netMask

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

# prints DNS info of the system
def printDNS():
    return None

# OS INFO

# STORAGE INFO

# PROCESSOR INFO

# MEMORY INFO

def main():
    # clear terminal 
    os.system("clear")

    # get hostname and domain via returnDevice()
    hostname, domain = returnDevice()

    # run logistics
    print("----- System Report -----\n"
          + "Device Information:\n"
          + "Hostname: " + hostname + "\n"
          + "Domain: " + domain + "\n\n"
          + "Network Information:\n"
          + "IPv4 Address: " + returnIP() + "\n"
          + "Default Gateway: " + defaultGate() + "\n"
          + "Network Mask: " + returnNetMask() + "\n"
          + printDNS()
          + "OS Information:\n"
          + "Operating System: " + returnIP() + "\n"
          + "Operating Version: " + returnIP() + "\n"
          + "Kernel Version: " + returnIP() + "\n")
    
if __name__ == '__main__':
    main()