#!/usr/bin/python3

#move files in a directory folder to trash bin
import os, send2trash, sys

#currentDIR
currentDir = os.listdir(os.getcwd())

userInput = sys.argv[1]

#iterate to the diretory
for i in currentDir:
    #check if the input is in the currentDir
    if userInput == i:
        #print deleting file.
        print(f"Deleting: {sys.argv[1]}")
        #deleting the folder/files
        send2trash.send2trash(i)

    #print error message.
    elif userInput != i:
        print(f"{sys.argv[1]} not in the directory")
        continue
