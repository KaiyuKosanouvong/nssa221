#!:/usr/bin/python3
# Kaiyu Kosanouvong / NSSA221 - Script 1
# runs a command line interface that performs a variety of network functions

# returns the default gateway of the system
def defaultGate():


# tests the local connection and returns a boolean
def localConnect():


# test remote connection and returns a boolean
def remoteConnect():


# tests the dns resolution
def dnsResolution():


# exits the program
def exit():


# sets up a command line menu for the user
def menu():
    str userInput = input("Please enter a command: \n" +
                      "(1) to get default gateway\n" +
                      "(2) to test local connection\n" +
                      "(3) to test remote connection\n" +
                      "(4) to test DNS resolution\n" +
                      "(5) to exit the program\n" +
                      "")
    
    match userInput:
        case "1":
            defaultGate()
            menu()
        case "2":
            localConnect()
            menu()
        case "3":
            remoteConnect()
            menu()
        case "4":
            dnsResolution()
            menu()
        case "5":
            exit()
        case _:
            menu()

def main():
    menu()
    