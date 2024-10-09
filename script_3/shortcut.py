#!/usr/bin/python3
# Kaiyu Kosanouvong / NSSA221 - Script 3 / October EEEEEEEEEEEEE, 2024
# creates and deletes system links. Can produce a report of existing links on the user's

# import os and pathlib modules
import os
import pathlib

def createLink(start, dest):
    # convert path to absolute file path
    startPath = pathlib.Path.home().__str__
    destPath = pathlib.Path.home().__str__

    # make link
    os.symlink(startPath,destPath)
    print("Link created from ", start, " to ", dest)

def deleteLink(start, dest):
    # convert path to absolute file path

    print("Link deleted from", start, " to", dest)


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
            start = input("Choose file 1: ")
            dest = input("Choose file 2: ")
            createLink(start,dest)

        elif userInput == "2": # deletes a link
            # inputs will just be file names
            start = input("Choose file 1: ")
            dest = input("Choose file 2: ")
            deleteLink(start,dest)

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