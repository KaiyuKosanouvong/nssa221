#!/usr/bin/python3
# Kaiyu Kosanouvong / NSSA221 - Script 4 / November 8, 2024
# generates a report of attempted logins on a server using the provided syslog.log file

# import os, re, geoip (geolite2) modules
import os
import re
from geoip import geolite2

# can install geoip and geolite2 using:
# sudo python3 -m pip install python-geoip-python3
# sudo python3 -m pip install python-geoip-geolite2

# compile regular expression that looks for IPs
IP_FIND = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

# checks for failed entries with the message "Failed password for"
FAIL_FIND = "Failed password for"

def parse_file(file): # parses the given log file and saves the number of entries from an IP, the IP itself, and their 
    entries = {} # save entries in dictionary, ip as key

    try:

        with open(file) as fs: # open file and put each line in logs list
            logs = fs.readlines()

            for line in logs: # iterate over each line to check for failure
                try: 
                    if re.search(FAIL_FIND, line): # if line indicates a failed attempt, search for ip and add it to dictionary
                        ip = re.findall(IP_FIND, line)[0]
                        
                        if ip in entries: # if ip is already in dictionary, increment the count
                            entries[ip] += 1

                        else: # if ip is not in dictionary, add to it
                            entries[ip] = 1

                except: # if any exception occurs while parsing the file, continue the loop (skip over line)
                    continue

    except: # if file cannot be found/be opened, exit
        print("Error: File Error on", file)
        return 0

    return entries

def sortEntries(entries): # manually sorts the list of entries from the log file based on count in ascending order
    newEntries = []

    for entry in entries: # add entries to newEntries (convert from dictionary to list)
        ip = str(entry)
        count = str(entries[entry])
        newEntries.append([ip, count])
    
    size = len(newEntries)
    for i in range(size-1): # iterate through entries
        for j in range(size-i-1):
            if int(newEntries[j][1]) > int(newEntries[j+1][1]): # compare count values, check if new entry is greater than previous entry
                newEntries[j], newEntries[j+1] = newEntries[j+1], newEntries[j] # swap entries
    
    return newEntries
        

def report(): # prints out the reports 
    entries = parse_file("/home/student/syslog.log") # get parse file for all attempts
    
    # sort the entries based on count in ascending order
    sortedEntries = sortEntries(entries)

    # header showing date and fields
    write_rep = "Attacker Report - " + os.popen("date").read().strip() + "\n\nCOUNT\tIP ADDRESS\t\tCOUNTRY\n"

    # iterate over entry list and print information corresponding to each ip
    for entry in sortedEntries:
        ip = entry[0]
        count = entry[1]

        if (int(count) > 9): # if the number of failed attempts is 10 or more, add to string
            
            # get country from ip via geolite2
            location = re.findall(r"[country=']+\w\w+[']", geolite2.lookup(ip).__repr__())[0].strip().split("'")[1]

            write_rep += count + "\t" + ip + "\t\t" + location + "\n"
    
    print(write_rep)


def main():
    # clear terminal 
    os.system("clear")

    # run report
    report()

if __name__ == '__main__':
    main()