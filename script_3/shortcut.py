#!/usr/bin/python3
# Kaiyu Kosanouvong / NSSA221 - Script 3 / October EEEEEEEEEEEEE, 2024
# creates and deletes system links. Can produce a report of existing links on the user's

# import os and pathlib modules
import os
import pathlib

def createLink(start, link):
    # convert path to absolute file path
    startPath = str

    # make link
    try:
        # os.symlink(startPath,link)
        print("Link created from", startPath, " to", link)
    
    except:
        print("File Error:\nfilename not found: ")

def deleteLink(link):
    # convert path to absolute file path
    startPath = str

    try:
        print("Link deleted from", startPath, " to", link)

    except:
        print("File Error:\nsymbolic link not found:", link)

def runReport():
    return 0

def commandList():
    while True:
        # parse for user input
        userInput = input("Please enter a command: \n" +
                        "(1) to create a link\n" +
                        "(2) to delete a link\n" +
                        "(3) to run a report of current links\n" +
                        "(4) to exit the program\n\n")

        if userInput == "1": # creates a link 
            # inputs will just be file names
            start = input("Choose file to access: ")
            link = input("Choose file shortcut name: ")
            createLink(start,link)

        elif userInput == "2": # deletes a link
            # inputs will just be file names
            link = input("Choose file shortcut name: ")
            deleteLink(link)

        elif userInput == "3": # runs a report of links on the desktop
            print("running report...")
            runReport()

        elif userInput == "4": # exits the program
            print("exiting program...")
            exit()

        else: # invalid command case
            print("invalid command: ", userInput)

def main():
    # clear terminal 
    os.system("clear")

    # run command list until exit program 
    commandList()

if __name__ == '__main__':
    main()