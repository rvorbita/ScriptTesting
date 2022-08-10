# #option 1 

# with open('prime.txt', 'r') as f:

#     line = f.read()
#     list1 = line.split('\n')
#     # print(list1)


# with open('happy.txt', 'r') as f:

#     line = f.read()

#     list2 = line.split('\n')
#     # print(list2)

# list3 = []

# for i in list1:

#         if i in list2:

#             list3.append(i)

# print(list3)





def prime_num(file):

    with open(file, 'r') as f:

        prime = list(f.read().split("\n"))

    return prime



def happy_num(file):

    with open(file, 'r') as f:

        happy = list(f.read().split("\n"))

    return happy


#create an instance 
myprime = prime_num('prime.txt')
myhappy = prime_num('happy.txt')


#list comprehenstion
result = [ i for i in myprime if i in myhappy ]

print(result)


