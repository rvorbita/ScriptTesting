# import random

# # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]



# a = random.sample(range(100), 10)
# print(a)

# b = random.sample(range(100), 15)
# print(b)

# new_list = []

# set_a = set(a)
# set_b = set(b)

# for i in set_a:

#     if i in set_b:

#         new_list.append(i)

# print(f"Common number for both a & b is/are {new_list}")



#ask for prime number




# def check_prime_number(n):

#     count = 2 

#     while count < n:
#         if n % count == 0:
#             return False
#         else:
#            return True
#     count += 1



# n = int(input("Enter a number: "))
# check_prime = check_prime_number(n)


# if check_prime:
#     print(f"{n} is a prime number.")
# else:
#     print(f"{n} is not a prime number.")



#list ends

# import random

# r_list = random.sample(range(30), random.randint(1,10))

# def start_end(list):

#     #append both start and end of a list to create a new list,
#     #shorcut to creating a list start and end.
#     new_list = [list[0], list[-1]]

#     # for i in list:
#     #     if i == list[0]:
#     #         new_list.append(list[0])
        
#     #     if i == list[-1]:
#     #         new_list.append(list[-1])

#     return new_list



# my_list = start_end(r_list)

# print(f"Your list is {r_list}")
# print(f"Converting your list to get START and END list {my_list}")



#list check duplicate.


a = ["mac", "cream", "shin", "cream", "mac", "void", "boid", "void"]


#using list
def list_duplicate_checker(list):

    new_list = []

    for i, v in enumerate(list):

        if v not in new_list:
            new_list.append(v)

    return new_list

print(list_duplicate_checker(a))



#using set
def list_duplicate_checker2(list):
    
    # using list
    # make_set = set(list)
    # new_list = []

    # for i in make_set:
    #     new_list.append(i)
    
    #return new_list
    
    #pure set
    make_set = set()
    for i in list:
        make_set.add(i)

    return make_set

print(list_duplicate_checker2(a))









