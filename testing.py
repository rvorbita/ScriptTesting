# import os

# currentDir = os.getcwd()

# def currentDirCount(folder):

#     folder = os.path.abspath(folder)

#     print(f"Counting the number of subfolder and files in {folder}")
#     print("")

#     f_count = 0
#     sdir_count = 0

#     for folderName, subFolders, files in os.walk(folder):
#         for file in files:
#             print(file)
#             f_count += 1
        
#         for subFolder in subFolders:
#             sdir_count += 1


#     print(f"Number of files in {folder} are {f_count}")
#     print(f"Number of subfolder in {folderName} are {sdir_count}")



# directory = input("Enter a directory: ")

# currentDirCount(directory)


d_list = [5,5,5,33,5,100,12,24,33]



def remove_dup(a):
    #convert the current list to dict, and convert back to a list.
    return list(dict.fromkeys(a))


print(remove_dup(d_list))