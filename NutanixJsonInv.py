#!/usr/bin/python3
# nutanixInv.py

import json
import glob2
from difflib import get_close_matches


# finds data in current folder and opens it
def findfiles(opt):
    wvm = ""
    l_files = glob2.glob("*.json")
    for item in l_files:
        data = json.load(open(item))
        if opt == 1:
            print(1)
        elif opt == 2:
            print(2)
        elif opt == 3:
            if wvm == "":
                wvm = input("Enter your machine name: ")
                for mitem in data:
                    if wvm == mitem['VM Name']:
                        print(mitem['VM Name'])

                    elif len(get_close_matches(wvm, mitem.keys()))>0:
                        guess = input("Did you mean %s instead (y/n)? " % get_close_matches(wvm, mitem.keys())[0])
                        if guess.lower() == "yes" or guess.lower() == "y":
                            print(mitem['VM Name'])
                    
                    elif len(get_close_matches(wvm, mitem.keys()))<=0:
                        print("no items to be found")

            else:
                for mitem in data:
                    if wvm == mitem['VM Name']:
                        print(mitem['VM Name'])
        
        else:
            print("What are you even doing here?")

"""
def render():
                    for mitem in data:
                    if wvm == mitem['VM Name']:
                        print("\nMachine found: \n")
                        print("Name: ", mitem['VM Name'])
                        print("IP: ", mitem['IP Addresses'])
                        print("CPU Cores: ", mitem['Cores'])
                        print("Ram: ", mitem['Memory Capacity'])
                        print("Flash: ", mitem['Flash Mode'])
                        print("\nResources currently in use: \n")
                        print("CPU Usage: ", mitem['CPU Usage'])
                        print("Ram Usage: ", mitem['Memory Usage'])
                        print("Disk usage: ", mitem['Storage'])
                        print("Write IOPS: ", mitem['Controller Write IOPS'])
                        print("Avg IO Latency", mitem['Controller Avg IO Latency'])
                        print("\n")

"""                        
# specifying data
def finetuning(opt):
    if opt == 1:
        print("Inventory printing\n")
        my_files = findfiles()
        getsrcdata(my_files)
    elif opt == 2:
        print("Resource printing\n")
    elif opt == 3:
        print("Find a vm")
        findfiles(3)
    else:
        print("What are you even doing here?")



# Iterate until valid Menu option is chosen
opt = 'nope'
while type(opt) != int:
    print("*** Menu ***")
    print("1. Print inventory")
    print("2. Print resources")
    print("3. Find a VM")
    print("4. Exit")
    opt = input("Pick an option: ")
    try:
        opt = int(opt)
    except:
        print("\nThat's not a valid option\n")
        opt = 'nope'

if opt == 1:
    finetuning(1)
elif opt == 2:
    finetuning(2)
elif opt == 3:
    finetuning(3)
else:
    print("... Exiting ...")


