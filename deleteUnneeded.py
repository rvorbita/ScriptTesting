#program that walks through a folder tree and searches for large
#files and folders.


import  os, send2trash


folder = input("Enter the folder absolute path: ")
threshold = input("Enter the maximum file size that you'd like to ignore in (megabytes): ")

for folderName, subFolders, fileNames in os.walk(folder):

    for filename in fileNames:

        size = os.path.getsize(os.path.join(folder, filename))
        
        if size > int(threshold) * 10 **6:
            print(f"File Found: {filename} | Size: {size // 10 ** 6 } | Source Path: {os.path.join(folder, filename)}")


