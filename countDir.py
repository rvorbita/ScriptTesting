#Find the folder in a directory tree that has the greatest
#number of files or the folder that uses the most disk space.

import os, shutil, glob

currentDir = os.getcwd()

def countDir(folder):
    #get the current absolute path.
    folder = os.path.abspath(folder)

    count = 0
    for folderName, subFolders, fileNames in os.walk(folder):
        print(f"Counting files inside folder {folderName}...")
        for filename in fileNames:
            count += 1

        print(f"There are {count} files in the {folderName}..")
        print("")

countDir('/home/raymart/Documents/testing_folder/folder3')