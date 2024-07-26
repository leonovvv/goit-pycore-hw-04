import sys
import os
from colorama import init, Fore

def display_path(dir_path, depth = 0):
    #Input validation
    if not os.path.isdir(dir_path):
        print('Input value is not a valid directory path')
        return

    #Print current folder name in blue
    print(Fore.BLUE + ' '*depth + os.path.basename(dir_path))
    for entity in os.listdir(dir_path):
        curr_path = os.path.join(dir_path, entity)
        if os.path.isdir(curr_path):
            #If current entity is folder - display it recursively with 1 more space
            display_path(curr_path, depth + 1)
        else:
            #Print current file name in yellow
            print(Fore.YELLOW + ' '*(depth+1) + entity)

#Colorama lib initialization
init()

if len(sys.argv) < 2:
    print('Insert path to view as command line argument')
    exit()

display_path(sys.argv[1])