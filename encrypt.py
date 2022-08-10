#encription and decription script.
#using cryptography , fernet
from cryptography.fernet import Fernet

# #string message
# msg = "Hello World"

# #generate a key for encription and decription script.
# key = Fernet.generate_key()

# #make an instance for the fernet class with the key generated
# fernet = Fernet(key)

# #use the fernet class instance.
# #to encrypt the string, string must be encoded
# #to byte string before encryption.

# encMSG = fernet.encrypt(msg.encode())
# print(f"Original string: {msg}")
# print(f"Encripted string: {encMSG}")

def generate_key():
    #Generate a key and save it in a file.
    key = Fernet.generate_key()
    with open("secret_key", "wb") as key_file:
        key_file.write(key)

def load_key():
    #Load the previously generated key.
    return open("secret_key", "rb").read()

def encrypt(str, key):
    #encript the string.
    f = Fernet(key)
    encMSG = f.encrypt(str.encode("utf-8"))
    return encMSG

def decrypt(str, key):
    f = Fernet(key)
    #decript the encripted string
    decMSG = f.decrypt(str).decode("utf-8")
    return decMSG


key = load_key()

while True:

    #MENU
    print("""
            SIMPLE STRING Encryption
            By: MC2022

            MENU: 
            1. Encrypt
            2. Decrypt 
            3. Quit
        
        """)

    menu = input("Enter your choice: ")

    if menu == '3':
        break

    if menu == '1':
        msg = input("provide a word: ")
        print("Generating encryption key.")
        print("Encrypting message...")
        enc = encrypt(msg, key)
        print(f"Message Successfuly Encryted : {enc}")


    if menu == '2':
        msg = bytes(input("Paste the encryted string: "), encoding='utf-8')
        print("Decrypting the message...")
        print(decrypt(msg, key))