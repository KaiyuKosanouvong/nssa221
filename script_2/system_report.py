#!/usr/bin/python3
# Kaiyu Kosanouvong / NSSA221 - Script 2 / September 27, 2024
# runs a diagnostic on the host system covering various specifications

# import os, netifaces, and platform modules
# to get netifaces:
# pip install netifaces
import os
import netifaces
import platform

# store hostname to use in log file
hostname = ""
# DEVICE INFO

# returns the device information of the system: hostname, Domain
def returnDevice():
    # store hostname as variable
    hostname = os.popen("hostname -s").read().strip("\n")
    # get host domain
    hostdomain = os.popen("hostname -f | sed -e 's/^"+hostname+"\.//'").read().strip("\n")

    return (hostname, hostdomain)

# NET INFO

# returns IP address of system
def returnIP():
    # get ip
    ip = os.popen("ip r |grep '^default' |awk '{print $9}'").read().strip("\n")

    return ip

# return network mask
def returnNetMask():
    # use netstat to get netmask via column formatting
    netMask = os.popen("netstat -nr |grep '^'|awk '{print $3}'").read().strip().split("\n")[3]
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

# fetches DNS info from the system
def getDNS():
    # get servers from /etc/resolv.conf file
    servers = os.popen("cat /etc/resolv.conf |grep '^nameserver' |awk '{print $2}'").read().strip().split('\n')

    # for each server registered in system, add to string
    counter = 0
    serverString = ""
    while (counter < servers.__len__()):
        # add to string & increment counter
        serverString += "DNS" + str(counter+1) + ":                  " + servers[counter] + "\n"
        counter += 1
    serverString += "\n"

    # return servers in printable format
    return serverString

# OS INFO

# retrieves operating system name, version, and kernel version
def getOS():
    osName = os.popen("head /etc/os-release -n 2 |grep '^NAME=' |sed -e 's/^NAME=//'").read().strip()
    osVers = os.popen("head /etc/os-release -n 2 |grep '^VERSION=' |sed -e 's/^VERSION=//'").read().strip()

    return (osName, osVers, platform.release())


# STORAGE INFO

# gets the total and available storage space in the /dev/mapper/rl-root drive
def getStorage():
    # use df with 
    return os.popen("df -Ph / |grep -v ^File | awk '{print $2, $4}'").read().strip().split(" ")
    

# PROCESSOR INFO

# fetches cpu name from os
def getCPUName():
    # use lscpu to retrieve cpu name
    return os.popen("lscpu |grep '^Model name: ' |awk '{print $3, $4, $5, $6}'").read().strip("\n")

# gets the number of CPU processors and cores 
def getProcsCores():
    # use lscpu
    cores = os.popen("lscpu |grep '^CPU(s):' |awk '{print $2}'").read().strip("\n")
    procs = os.popen("lscpu |grep '^Socket(s):' |awk '{print $2}'").read().strip("\n")

    return procs, cores

# MEMORY INFO
def getRAM():
    # run command to get memory values in gigabytes
    return os.popen("free -g |grep '^Mem:' |awk '{print $2} {print $4}'").read().strip().split("\n")
    

def main():
    # clear terminal 
    os.system("clear")

    # get hostname and domain via returnDevice()
    hostname, domain = returnDevice()

    # get storage info
    totalDrive, availDrive = getStorage()

    # get OS info
    op_system, op_version, kern_version = getOS()

    # get number of processors and cores
    procs, cores = getProcsCores()
    
    # get total and available ram via getRAM
    totalRAM, availRAM = getRAM()

    # run logistics
    report = ('System Report @ ' + os.popen('date').read().strip() + '\n'
          + 'Device Information:\n'
          + 'hostname:              ' + hostname + '\n'
          + 'Domain:                ' + domain + '\n\n'

          + 'Network Information:\n'
          + 'IPv4 Address:          ' + returnIP() + '\n'
          + 'Default Gateway:       ' + defaultGate() + '\n'
          + 'Network Mask:          ' + returnNetMask() + '\n'
          + getDNS()

          + 'OS Information:\n'
          + 'Operating System:      ' + op_system + '\n'
          + 'Operating Version:     ' + op_version + '\n'
          + 'Kernel Version:        ' + kern_version + '\n\n'

          + 'Storage Information:\n'
          + 'Hard Drive Capacity:   ' + totalDrive + '\n'
          + 'Available Space:       ' + availDrive + '\n\n'

          + 'Processor Information:\n'
          + 'CPU Model:             ' + getCPUName() + '\n'
          + 'Number of Processors:  ' + procs + '\n'
          + 'Number of Cores:       ' + cores + '\n\n'

          + 'Memory Information:\n'
          + 'Total RAM:             ' + totalRAM + 'GB\n'
          + 'Available RAM:         ' + availRAM + 'GB\n')
    
    os.popen("printf '"+report+"' |tee /home/student/Scripts/SA2/"+hostname+"_system_report.log")

if __name__ == '__main__':
    main()