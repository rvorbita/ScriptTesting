#!/bin/python3
import random

#function to generate password.
def password_gen(n):

    #random value
    word_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345678910!@#$%*"
    #value placeholder.
    password = ""


    for i in range(n):

        p = random.choice(word_list)
        password += p


    return password


#loop until user wants to quit.
while True:

    print(""" 

        Welcome to Py Password Generator
        
        created by: MC2022

        How to use:

        Choose from the Menu below

        1. Weak Password ( 8 characters ) 
        2. Normal Password ( 16 characters )
        3. Hard Password ( 32 characters )
        4. Quit

    """)


    user = input(">> ")

    generated_password = ""

    #condition to check if user want's to quit.
    if user == '4':
        print("Thank you bye.")
        break
    else:

        if user == '1':
            #manual input of length.
            generated_password = password_gen(8)

        elif user == '2':
        
            #manual input of length.
            generated_password = password_gen(12)

        elif user == '3':
            #manual input of length.
            generated_password = password_gen(16)
        
        
        print("Starting to generate the password...")
        print("")
        print(f"Password generated successfully >> '{generated_password}'")
        print("")





