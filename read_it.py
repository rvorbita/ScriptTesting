#Given a .txt file that has a list of a bunch of names,
#count how many of each name there are in the file, 
#and print out the results to the screen. 
#I have a .txt file for you, if you want to use it!




#task 1

# char_dict = {}


# with open('starwars.txt', 'r') as f:

#     line = f.readline()

#     while line: 

#         line = line.strip()

#         if line in char_dict:

#             char_dict[line] += 1

#         else:

#             char_dict[line] = 1


#         line = f.readline()


#     print(char_dict)




#task 2

char_dict = {}


with open('sun.txt', 'r') as f:

    line = f.readline()

    while line: 

        line = line[3:-26]

        if line in char_dict:

            char_dict[line] += 1

        else:

            char_dict[line] = 1


        line = f.readline()


for k,v in char_dict.items():

    print(f"Name: {k}, = {v}")
