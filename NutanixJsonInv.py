#!/usr/bin/python3
# nutanixJsonInv.py

# pip install glob2 in case you don't have the module.
# 1) Export from Nutanix (Prism Element) console > VM > Json
# 2) Copy the files in the same directory as this script
# 3) run the script. 

import json
import glob2
from difflib import get_close_matches

# finds data in current folder, opens it and returns the content
def openfile():
    l_files = glob2.glob("*.json")
    data = []
    for item in l_files:
        data.append(json.load(open(item)))
        
    return data


# get into the options and work with the data
def handleoptions(opt, data):
    if opt == 1:
        i = 0
        for sepfiles in data:
            for lines in sepfiles:
                print(lines['VM Name'])
                i +=1
        print("Total items: ", i)

    elif opt == 2:
        findme = input("Enter your device name: ")
        lmachines = []
        result = False
        for sepfiles in data:
            for lines in sepfiles:
                lmachines.append(lines['VM Name'])
                if (findme == lines['VM Name']) or (findme.lower() in lines['VM Name']) or (findme.capitalize() in lines['VM Name']):
                    result = True
                    print("\nMachine found: \n")
                    print("Name: ", lines['VM Name'])
                    print("IP: ", lines['IP Addresses'])
                    print("CPU Cores: ", lines['Cores'])
                    print("Ram: ", lines['Memory Capacity'])
                    print("Flash: ", lines['Flash Mode'])
                    print("\nResources currently in use: \n")
                    print("CPU Usage: ", lines['CPU Usage'])
                    print("Ram Usage: ", lines['Memory Usage'])
                    print("Disk usage: ", lines['Storage'])
                    print("Write IOPS: ", lines['Controller Write IOPS'])
                    print("Avg IO Latency", lines['Controller Avg IO Latency'])
                    print("\n")

        if not result:    
            if get_close_matches(findme,lmachines):
                print("Could not find the name you mentioned... I found this one: %s" % get_close_matches(findme,lmachines)[0])
                opts = input("Is this the one you are searching for (y/n) ")
                if opts.lower() == 'y' or opts.lower() == "yes":
                    findme = get_close_matches(findme,lmachines)[0]
                    for sepfiles in data:
                        for lines in sepfiles:
                            if findme == lines['VM Name']:
                                print("\nMachine found: \n")
                                print("Name: ", lines['VM Name'])
                                print("IP: ", lines['IP Addresses'])
                                print("CPU Cores: ", lines['Cores'])
                                print("Ram: ", lines['Memory Capacity'])
                                print("Flash: ", lines['Flash Mode'])
                                print("\nResources currently in use: \n")
                                print("CPU Usage: ", lines['CPU Usage'])
                                print("Ram Usage: ", lines['Memory Usage'])
                                print("Disk usage: ", lines['Storage'])
                                print("Write IOPS: ", lines['Controller Write IOPS'])
                                print("Avg IO Latency", lines['Controller Avg IO Latency'])
                                print("\n")
                else:
                    print("\nHmm, these are the ones I found, try the program again with one of those names:")
                    foundall = get_close_matches(findme,lmachines,5)
                    for fitem in foundall:
                        print(fitem)


    else:
        for sepfiles in data:
            for lines in sepfiles:
                if not lines['IP Addresses']:
                    print("Offline: ", lines['VM Name'])
        
                   
# Start Program
# Iterate until valid Menu option is chosen
opt = 99
while (opt > 4 or opt <= 0 ):
    print("\n*** Menu ***")
    print("1. Print inventory")
    print("2. Find a VM")
    print("3. Print Offline VM's")
    print("4. Exit")
    opt = input("Pick an option: ")
    try:
        opt = int(opt)
    except ValueError:
        print("\nThat's not a valid option\n")
        opt = 99

# Calling quit() before testing of files
if opt == 4:
    print("\n... Exiting ...\n")
    quit()

# Load file if files are available, make layout nice
content = openfile()

if content:
    if opt == 1:
        handleoptions(1, content)
    elif opt == 2:
        handleoptions(2, content)
    elif opt == 3:
        handleoptions(3, content)
    else:
        print("\n... Exiting ...\n")
        quit()
else:
    print("\nNo json files found, please place them in them in the same directory as the script.")
    print("... Exiting ...\n")
    quit()

