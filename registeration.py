import time
import os
import re
import login
data = open("dataRegister.txt", "r")
users = data.readlines()
print("---------------- registeration ---------------- ")

############################# FirstName #############################


def validateFirstName():
    FirstName = input("please enter your FirstName : ")
    while not FirstName.isalpha():
        print("Not Valid Name")
        FirstName = input("please enter your FirstName : ")
    else:
        return FirstName


FirstName = validateFirstName()

############################# LastName #############################


def validateLastName():
    LastName = input("please enter your LastName : ")
    while not LastName.isalpha():
        print("Not Valid Name")
        LastName = input("please enter your LastName : ")
    else:
        return LastName


LastName = validateLastName()

############################# Email #############################


def validatingEmail():

    email = input("please enter your email : ")
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Not Valid email")
        email = input("please enter your email : ")

    else:
        for x in range(len(users)):
            while users[x].split(":")[3] == email:
                print(f"{email} is already registered ")
                print("enter a new email")
                email = input()
    return email


email = validatingEmail()

############################# Password #############################


def validatePassword():
    password = input("please enter your Password : ")
    import re
    while len(password) < 8 or not re.search('[0-9]', password) or not re.search('[A-Z]', password):
        print("Not Valid password is at lest 8 letters or has a number in it or has a capital letter in it")
        password = input("please enter your Password : ")
    else:
        return password


password = validatePassword()

############################# ConfirmPassword #############################


def validateConfirmPassword():
    ConfirmPassword = input("please enter your ConfirmPassword : ")
    while not ConfirmPassword == password:
        print("Not Valid ConfirmPassword")
        ConfirmPassword = input("please enter your ConfirmPassword : ")
    else:
        return ConfirmPassword


ConfirmPassword = validateConfirmPassword()

############################# Phone #############################


def validatePhone():
    Phone = input("please enter your Phone : ")
    import re
    while not re.match(r"^01[0-9]{9}$", Phone):
        print("Not Valid Phone")
        Phone = input("please enter your Phone : ")
    else:
        for x in range(len(users)):
            while Phone in users[x].split(":")[5]:
                print(f"{Phone} is already registered ")
                print("enter a new Phone")
                Phone = input()
    return Phone


Phone = validatePhone()

################################################################


def addData():
    id = round(time.time())
    file_data = open("dataRegister.txt", 'a')
    file_data.write(
        f"{id}:{FirstName}:{LastName}:{email}:{password}:{Phone} \n")
    file_data.close()
    login.validatelogin()


data = addData()
################################################################
