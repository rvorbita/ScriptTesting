#Write a program that walks through a folder tree and searches 
#for files with a certain file extension (such as .pdf or .jpg). 
#Copy these files from whatever location they are in to a new folder.

import os, shutil


folder = input("Enter the absolute path of the folder: ")
extension = input("Enter the extension of files to be copied: ")
destination = input("Enter the absolute path for destination: ")


for folderName, subFolders, fileNames in os.walk(folder):

    for filename in fileNames:
        #check for search extension.
        if filename.endswith(extension):
            shutil.copy(os.path.join(folder, filename), destination)

    print(f"Done Copying files from {os.path.basename(folder)} and move to {os.path.basename(destination)}")
