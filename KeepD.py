import os
Names=[]
Surnames=[]
Emails=[]
EmailsWoFo=[]
Passwords = ['Egef_14896','E142_1489as6','Adam_1456','Er_12as25sa','Ar7_Cr98','Sak_1523as','Fet_14h22','Merh_13579','Ea_123ae','D_fg275w','Son_248s6']
UsrPasswds=[]
Numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
nlin="https://mail.tm/tr/"

if os.path.exists("user_names.txt"):
    with open("user_names.txt", "r") as file:
        Names = file.read().splitlines()
if os.path.exists("last_names.txt"):
    with open("last_names.txt", "r") as file:
        Surnames = file.read().splitlines()
if os.path.exists("EmailWithFormat.txt"):
    with open("EmailWithFormat.txt", "r") as file:
        Emails = file.read().splitlines()   
if os.path.exists("EmailWoFo.txt"):
    with open("EmailWoFo.txt", "r") as file:
        EmailsWoFo = file.read().splitlines()   
if os.path.exists("UserPasswords.txt"):
    with open("UserPasswords.txt", "r") as file:
        UsrPasswds = file.read().splitlines()
print(Names)
print(Surnames)
print(Emails)
print(EmailsWoFo)
print(UsrPasswds)