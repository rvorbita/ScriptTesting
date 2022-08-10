#output 0 1 1 2 3 5 8 13 .. 

# def fibonacci_generator(n):
#     a = 0
#     b = 1
#     for i in range(n):

#         print(a)
#         sum = a + b 
#         a = b
#         b = sum


# #ask user.
# nterms = int(input("Enter number of terms to generate >  "))


# if nterms <= 0:

#     print("Enter positive number of terms to generate")

# else:

#     #generate value
#     fibonacci_generator(nterms)



#new_list = [ i for i in range(10) if i % 2 == 0]
#print(new_list)


#divisor checking
# user = int(input("Enter a number > "))
# num_range = int((input("Enter number range > ")))
# new_list = []


# for i in range(1, num_range):

#     if i % user == 0:
#         new_list.append(i)


# print(new_list)


#list overlapping
#create a random list of overlapping


#manual
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = list(set(a+b))
# c.sort()
# print(c)


#with randomnumber.
# import random

# list_a=[]
# list_b=[]

# def GenRadList(list):

#     #Generate a Random List of number overlapping

#     for i in range(0, random.randint(1, 20)):

#         n = random.randint(1,20)

#         list.append(n)

#     print(f"List Generated: > {list}")




# def CheckList(a,b):

#     new_list = []

#     #check for common number.
#     for i in b:
#         if i in a:
#             if i not in new_list:
#                 new_list.append(i)

#     new_list.sort()
#     print(f"Common in both A and B List are {new_list}")

# GenRadList(list_a)
# GenRadList(list_b)
# CheckList(list_a, list_b)




#StringList
# myString=input("Enter a Panderome word > ").lower()
# reverse = myString[::-1].lower()
# newString= ""

# if myString.isalpha():

#     if myString.lower() == reverse.lower():
#         print("Word is panderome")
#     else:
#         print("Word is not panderome")

# else:

#     print("Provide only String.")



#LIST COMPREHENSIONS
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def gen_newlist(a):

    new_list = [ i for i in a if i % 2 == 0]

    return new_list

print(gen_newlist(a))











