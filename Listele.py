import os
from NameAndSurname import first_names,last_names
from CreateEmail import emwofo,emailwfo,mail,letters_list_to_str,chars_after_at,email_format
from KeepD import Passwords

import random
adList = []
soyadList= []
Email=[]
EmailWofo=[]
UsePassw=[]


if os.path.exists("user_names.txt"):
    with open("user_names.txt", "r") as file:
        adList = file.read().splitlines()
if os.path.exists("last_names.txt"):
    with open("last_names.txt", "r") as file:
        soyadList = file.read().splitlines()
if os.path.exists("EmailWithFormat.txt"):
    with open("EmailWithFormat.txt", "r") as file:
        Email = file.read().splitlines()
if os.path.exists("EmailWoFo.txt"):
    with open("EmailWoFo.txt", "r") as file:
        EmailWofo = file.read().splitlines()
if os.path.exists("UserPasswords.txt"):
    with open("UserPasswords.txt", "r") as file:
        UsePassw = file.read().splitlines()



while True:
    print("1. Add user")
    print("2. Delete user")
    print("3. View users")
    print("4. Quit")
    print("5. Delete all users")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        
        
        #adSoyad = input("Enter name and surname: ")
        adList.append(random.choice(first_names))
        soyadList.append(random.choice(last_names))
        asd=("".join(random.choices(letters_list_to_str,k=chars_after_at)))
        Email.append(asd+email_format)
        EmailWofo.append(asd)
        UsePassw.append(random.choice(Passwords))
    elif choice == 2:
        adSoyad = input("Enter the name and surname of the user to delete: ")
        if adSoyad in adList:
            adList.remove(adSoyad)
        else:
            print("User not found.")
    elif choice == 3:
        print(adList)
        print(soyadList)
        print(Email)
        print(EmailWofo)
        print(UsePassw)
    elif choice == 4:
        with open("user_names.txt", "w") as file:
            for name in adList:
                file.write(name + "\n")
        with open("last_names.txt", "w") as file:
            for surname in soyadList:
                file.write(surname + "\n") 
        with open("EmailWithFormat.txt", "w") as file:
            for email in Email:
                file.write(email + "\n")  
        with open("EmailWoFo.txt", "w") as file:
            for emailWoF in EmailWofo:
                file.write(emailWoF + "\n")  
        with open("UserPasswords.txt", "w") as file:
            for UPassw in UsePassw:
                file.write(UPassw + "\n")     
        break
    elif choice == 5:
        adList = []
        soyadList=[]
        Email=[]
        EmailWofo=[]
        UsePassw=[]
        print("All users deleted.")
    else:
        print("Invalid choice. Try again.")

