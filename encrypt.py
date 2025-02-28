import caesarCypher
import rsa
import binary
import os

# Open file, retrieve data, then close file
file = open("data.txt", "rt")
content = file.read()
file.close()

# Ask user what encryption method they want to use
print("1: Binary")
print("2: Caesar Cypher")
print("3: RSA")
method = input("Please Enter The Corresponding Number Of The Encryption Method You Wish To Use: ")
if method == "1":
    print("You Have Selected The Binary Encryption Method.")
elif method == "2":
    print("You Have Selected The Caesar Cypher Encryption Method.")
elif method == "3":
    print("You Have Selected The RSA Encryption Method.")
else:
    print("Uh Oh, Please Try Again And Enter A Number Corresponding To The Method You Wish To Use.")

encryptedText = ""

# Binary Encryption
if method == "1": 
    encryptedText = binary.encrypt(content)
    

# Caesar Cypher Encryption
if method == "2": 
    encryptedText = caesarCypher.encrypt(content)
    
    
# RSA Encryption
if method == "3": 

    e, d, n = rsa.generateKeys()
    print(f"\nHere is your public key (e, n): {e} || {n}\n")
    print(f"\nHere is your private key (d, n), 'Do not share this with anyone': {d} || {n}\n")

    encryptedText = rsa.encrypt_text(content, e, n)
    print("[Encryption Successful!]\n")
    

# Open file, write data, then close file
file = open("data.txt", "w")
file.write(str(encryptedText))
file.close()