
import random


#using non binary search
def normal_search(mylist, search):

    i = list(dict.fromkeys(mylist))
    number_of_iteration = 0

    print(i)

    for n in i:

        number_of_iteration += 1

        if search == n:

            print(f"number {search} found")
            print(f"number of iteration {number_of_iteration}")



#using binary searching.
def binary_search(mylist, number_to_search):
    #sorted number from 1 to xxx
    sorted_list = sorted(set(mylist))
    start = 0
    end = len(sorted_list)-1

    while start <= end:

        mid = (start + end ) // 2 #whole number hindi floating number or decimal.
        mid_value = sorted_list[mid]


        #check if the midvalue is equal to the number search
        #if yes. print the unsorted, sorted and the index position.
        if mid_value == number_to_search:
            print(f"sorted number {sorted_list}")
            print(f"Number found in index position {mid} ")
            break
        #else if number search is less than the mid value
        #assign the value of mid - 1 to the end.``
        elif number_to_search < mid_value:
            end = mid - 1
        #else assign the value of mid + 1 to the start
        else:
            start = mid + 1

        #first solution
        
        #check if mid value is less than the start value
        #check if mid value is greater than the end value
        #check if mid value is less than 0.
        #return number not found
        # if mid_value > end:
        #     print("Number not found")
            
    #second error solution
    return None
        
a = [11,1,3,4,6,7,8,9]
b = [1,2,3,4,5]

def generate_random_number(n):
    r_number = []
    for i in range(n+1):
        r_number.append(random.randint(0,30))

    return r_number




#simple task.

search = int(input("Enter number to be search > "))

if search > 0:
    n = int(input("Enter number range > "))
    number = generate_random_number(n)

    print(f"Unsorted List: {number}")
    binary_search(number, search)
else:
    print("enter only positive number and not letter.")




