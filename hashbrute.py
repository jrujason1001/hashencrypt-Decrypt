import hashlib, itertools
import os
import string
import sys
choice = int(input("Do you want to encrypt or decrypt a hash? 1 for encrypt, 0 for decrypt"))
if(choice == 1):
    user = input("Enter the string you want to hash: ")
    method = int(input("""Please enter the hashing method:
                   1. SHA256
                   2. MD5
                   3. SHA512
                   """))
    salt = int(input("Do you want to add the salt? type 1 for yes, 0 for no. "))
    def encrypt():
        if(method == 1):
            if(salt == 0):
                text = hashlib.sha256()
                text.update(user.encode("utf-8"))
                print(text.hexdigest())
            elif(salt == 1):
                text = hashlib.pbkdf2_hmac('sha256', user.encode("utf-8"), salt=os.urandom(16), iterations=1000)
                print(text.hex())
        if(method == 2):
            if(salt == 0):
                text = hashlib.md5()
                text.update(user.encode("utf-8"))
                print(text.hexdigest())
            elif(salt == 1):
                text = hashlib.pbkdf2_hmac('md5', user.encode("utf-8"), salt=os.urandom(16), iterations=1000)
                print(text.hex())

        if(method == 3):
            if(salt == 0):
                text = hashlib.sha512()
                text.update(user.encode("utf-8"))
                print(text.hexdigest())
            elif(salt == 1):
                text = hashlib.pbkdf2_hmac('sha512', user.encode("utf-8"), salt=os.urandom(16), iterations=1000)
                print(text.hex())
    encrypt()
elif(choice == 0):
    choice_hash_algo = int(input("""What is the hashing algorithm you want to crack? 
                       1. SHA256
                       2. MD5
                       3. SHA512
                       """))
    text = input("Enter the hash value: ")
    if(choice_hash_algo == 1):
        chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
        for n in range(1,32):
            for xs in itertools.product(chrs, repeat=n):
                original = ''.join(xs)
                m = hashlib.sha256()
                m.update(bytes(original, encoding='utf-8'))
                if m.hexdigest() == text:
                    print("String: " + original)
                    sys.exit()
    elif (choice_hash_algo == 2):
        chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
        for n in range(1,32):
            for xs in itertools.product(chrs, repeat=n):
                original = ''.join(xs)
                m = hashlib.md5()
                m.update(bytes(original, encoding='utf-8'))
                if m.hexdigest() == text:
                    print("String: " + original)
                    sys.exit()
    elif(choice_hash_algo == 3):
        chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
        for n in range(1,32):
            for xs in itertools.product(chrs, repeat=n):
                original = ''.join(xs)
                m = hashlib.sha512()
                m.update(bytes(original, encoding='utf-8'))
                if m.hexdigest() == text:
                    print("String: " + original)
                    sys.exit()
    
