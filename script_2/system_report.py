#!/usr/bin/python3
# Kaiyu Kosanouvong / NSSA221 - Script 2
# runs a diagnostic on the host system covering various specifications

# import os, netifaces, and platform modules
# to get netifaces:
# pip install netifaces
import os
import netifaces
import platform

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
# retrieves operating system name, version, and kernel version
def getOS():
    return (platform.system(), platform.version(), platform.release())


# STORAGE INFO
def getStorage():
    os.popen("df").read().strip().split("\n")

# PROCESSOR INFO
def getCPU():
    return os.popen("lscpu |grep '^Model name: ' |awk '{print $3} {print $4} {print $5} {print $6}'").read().strip()

# MEMORY INFO
def getRAM():
    # run command to get memory values in gigabytes
    return os.popen("free -g |grep '^Mem:' |awk '{print $2} {print $4}'").read().strip().split("\n")
    

def main():
    # clear terminal 
    os.system("clear")

    # get hostname and domain via returnDevice()
    hostname, domain = returnDevice()

    # get total and available ram via getRAM
    totalRAM, availRAM = getRAM()

    # get OS info
    op_system, op_version, kern_version = getOS()

    # run logistics
    print("----- System Report @ " + os.popen("date").read().strip() + " -----\n"
          + "Device Information:\n"
          + "Hostname:              " + hostname + "\n"
          + "Domain:                " + domain + "\n\n"

          + "Network Information:\n"
          + "IPv4 Address:          " + returnIP() + "\n"
          + "Default Gateway:       " + defaultGate() + "\n"
          + "Network Mask:          " + returnNetMask() + "\n"
        #   + printDNS()

          + "OS Information:\n"
          + "Operating System:      " + op_system + "\n"
          + "Operating Version:     " + op_version + "\n"
          + "Kernel Version:        " + kern_version + "\n\n"

          + "Storage Information:\n"
          + "Hard Drive Capacity:   " + returnIP() + "\n"
          + "Available Space:       " + returnIP() + "\n\n"

          + "Processor Information:\n"
          + "CPU Model:             " + returnIP() + "\n"
          + "Number of Processors:  " + returnIP() + "\n"
          + "Number of Cores:       " + returnIP() + "\n\n"

          + "Memory Information:\n"
          + "Total RAM:             " + totalRAM + "GB\n"
          + "Available RAM:         " + availRAM + "GB\n")
    
if __name__ == '__main__':
    main()