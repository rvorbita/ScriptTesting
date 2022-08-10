#create a fibonacci sequence
# 0 1 1 2 3 5 8 13 


def fibonacci_generator(n):

    a = 0
    b = 1
    for i in range(n):
        
        print(a)   
        sum = a + b
        a = b 
        b = sum 


if __name__ == "__main__":

    number = int(input("Enter number range: "))

    if number <= 0:
        print("Please enter positive number only.")
    else:
        print("Generater Fibonacci numbers")
        fib = fibonacci_generator(number)





