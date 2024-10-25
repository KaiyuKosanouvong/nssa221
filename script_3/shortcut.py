#!/usr/bin/python3
# Kaiyu Kosanouvong / NSSA221 - Script 3 / October 25, 2024
# creates and deletes system links. Can produce a report of existing links on the user's

# import os, pathlib modules
import os
import pathlib

# save desktop directory as a global variable
DESKTOP = pathlib.Path.home().__str__() + "/Desktop/"

# save current directory as a global variable
CURR_DIRECTORY = os.popen("pwd").read().strip()

def createLink(object): # creates a symbolic link to a given file

    if isLinked(object): # if the link has already been created in the Desktop directory
        print("Link/File already exists in ~/Desktop directory :", object)
        print(isLinked(object))

    else:
        paths = findFilePath(object) # get file path

        if (paths != 0):
            
            if paths.__len__() == 1: # if there is only one instance, make link_path the only path available
                link_path = paths[0]

            else: # if multiple instances of file exists, ask for input
                print("Multiple instances of the file", object, "have been found.\n"
                    + "Please select which file you would like to link:")
                counter = 1
                hit_list = ""
                
                for path in paths:
                    hit_list += "("+(str)(counter)+"): " + path + "\n"
                    counter += 1
                hit_list += "Press any other key to exit menu\n"
                inp = input(hit_list) # present user with options, scan for input

                if (int)(inp) >= 1 & (int)(inp) <= counter: # if valid input, set link path as assigned path
                    link_path = paths[(int)(inp)-1]
                
                else: # if any other key is pressed, exit out of createLink
                    return 0
            if isLinked(object): # if the link has already been created in the Desktop directory
                print("Link/File already exists in ~/Desktop directory :", object)
            print(isLinked(object))
            os.popen("ln -s " + link_path + " -t " + DESKTOP) # create link
            print("File path has been made to:", link_path, "via", object)
    

def deleteLink(link): # deletes link 
    
    if isLinked(link): # check if link exists in Desktop directory
        os.popen("rm " + DESKTOP + link)
        print("Link deleted:", link)

    else: # if no link exists in the desktop, print DNE error message
        print("Link does not exist:", link)

def isLinked(link): # check if link is exists in Desktop directory
    return os.path.exists(DESKTOP + link)

def findFilePath(target): # parse through top root directory to find instances of a target file
    
    hits = [] # buffer list to hold targets found
    try:

        list = os.walk("/") # use walk function to parse through entire root directory
        for dir in list:
            for file in dir[2]: # iterate through each file in directory until target is hit
                
                if file.__eq__(target): # if target is found, add to hits
                    hits.append(dir[0]+"/"+(file))
            
            for subdir in dir[1]: # iterate through each subdirectory in directory until target is hit
                
                if subdir.__eq__(target): # if target is found, add to hits
                    hits.append(dir[0]+"/"+(subdir))

        if hits.__len__() == 0: # if target is not found, return 0
            print ("File not found:", target)
            return 0
        
        else:
            return hits
        
    except: # if walk fails, print error message and return 0
        print("Exception occured during search.")
        return 0

def runReport(): # runs a report of the Desktop directory's active links
    
    links = os.popen("find ~/Desktop -type l").read().strip().split("\n")
    print("Symbolic links in Desktop Directory: ")

    if links.__len__() < 1: # if no links exist in Desktop, print empty string
        print("")

    else :
        for link in links: # print each link in the Desktop Directory
            linked_file_path = os.popen("readlink " + link).read().strip()
            print(link,"->", linked_file_path)

        return links

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
            createLink(start)

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

    # print out working directory:
    print("Current working directory:", CURR_DIRECTORY)

    # run command list until exit program 
    commandList()

if __name__ == '__main__':
    main()