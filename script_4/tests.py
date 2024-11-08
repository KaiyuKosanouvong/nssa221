import re
import os
from geoip import geolite2

def parse_file(file): # parses the given log file and saves the number of entries from an IP, the IP itself, and their 
    entries = dict()
    ip_find = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b') # compile regular expression that looks for IPs


    with open(file) as fs: # open file and put each line in logs list
        logs = fs.readlines()

        for line in logs: # iterate over each line
            try: 
                ip = re.findall(ip_find, line)[0] # use regular expression to see if the line contains an ip
                
                if ip in entries: # if ip is already in dictionary, increment the count
                    entries[ip][0] += 1

                else:
                    location = geolite2.lookup()
                    entries[ip] = [1, ip, location]

            except: # if any exception occurs while parsing the file, continue the loop
                continue

    return entries

def main():
    print(parse_file("/home/student/syslog.log").__len__())

if __name__ == '__main__':
    main()