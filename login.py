import os

name = ''


def validatelogin():
    print("---------------- login ---------------- ")

    email = input("please enter your email : ")
    import re
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Not Valid email")
        email = input("please enter your email : ")
    else:
        read_data = open("dataRegister.txt", 'r')
        data = read_data.readlines()
        for x in range(len(data)):
            if data[x].split(":")[3] == email:
                passw = data[x].split(":")[4]
                global name
                name = data[x].split(":")[1]
                password = input("please enter your Password : ")
                while not password == passw:
                    print("wrong")
                    password = input("please enter your Password : ")
                else:
                    if f"{name}" not in os.listdir():
                        os.system("mkdir {name}Projects".format(name=name))
                        print(f"{name}Project Directory Created")
                    ######################### MenuProject #########################

                        def project(name):
                            print("-------------- MenuProject --------------")

                            def MenuProject():
                                print("(1) create project")
                                print("(2) view all project")
                                print("(3) delete your project")
                                print("(4) update your project")
                                print("(5) Exit")

                            MenuProject()
                            option = input("enter your option: ")
                            while option != "1" and option != "2" and option != "3" and option != "4" and option != "5":
                                option = input(
                                    "please choose 1 or 2 or 3 or 4 or 5 only")
                            else:
                                ############################## create project #########################

                                if option == "1":
                                    os.system("clear")
                                    file = input("enter your file name : ")
                                    while not file.isalpha():
                                        print("invalid input")
                                        file = input("enter your file name : ")
                                    else:

                                        os.system(
                                            f"cd {name}Projects && touch {file}")
                                        title = input("enter your title: ")
                                        while not title.isalpha():
                                            print("not valid (empty)")
                                            title = input("enter your title: ")
                                        else:
                                            Details = input(
                                                "enter your Details: ")
                                            while Details == "":
                                                print("not valid (empty)")
                                                Details = input(
                                                    "enter your Details: ")
                                            else:
                                                Target = input(
                                                    "enter your Target: ")
                                                while not Target.isnumeric():
                                                    print(
                                                        "please enter numbers")
                                                    Target = input(
                                                        "enter your Target : ")
                                                else:
                                                    Target_data = open(
                                                        f"{name}Projects/{file}", 'w')
                                                    Target_data.write(
                                                        f"title is : {title} \n Details is : {Details } \n Target is : {Target} \n")
                                                    Target_data.close()
                                                    project(name)

                        ######################### view all project #########################

                                elif option == "2":
                                    os.system("clear")
                                    os.system(f"cd {name}Projects && ls")
                                    project(name)

                        ######################### Deleted project #########################

                                elif option == "3":
                                    os.system("clear")
                                    delete = input(
                                        "enter your project name you want to delete: ")

                                    while not f"{delete}" in os.listdir(f"/home/lenovo/Desktop/ITI/ITI Labs/Python/lab3/{name}Projects"):

                                        print("this project isn't exist")
                                        delete = input(
                                            "enter your project name you want to delete: ")
                                    else:
                                        os.system(
                                            f"cd {name}Projects && rm -r {delete}")
                                        print(f"{delete} deleted successfully")
                                        project(name)
                        ######################### update project #########################

                                elif option == "4":
                                    os.system("clear")
                                    edit = input(
                                        "enter name of the prjoect you want to edit : ")
                                    while not f"{edit}" in os.listdir(f"/home/lenovo/Desktop/ITI/ITI Labs/Python/lab3/{name}Projects"):
                                        print("this project isn't exist")
                                        edit = input(
                                            "enter name of the prjoect you want to edit")
                                    else:
                                        title = input("enter your title: ")
                                    while not title.isalpha():
                                        print("not valid (empty)")
                                        title = input("enter your title: ")
                                    else:
                                        Details = input("enter your Details: ")
                                        while Details == "":
                                            print("not valid (empty)")
                                            Details = input(
                                                "enter your Details: ")
                                        else:
                                            Target = input(
                                                "enter your Target: ")
                                            while not Target.isnumeric():
                                                print("please enter numbers")
                                                Target = input(
                                                    "enter your Target : ")
                                            else:
                                                Target_data = open(
                                                    f"{name}Projects/{Target}", 'w')
                                                Target_data.write(
                                                    f"title is : {title} \n Details is : {Details } \n Target is : {Target} \n")
                                                Target_data.close()
                                                project(name)

                        ############################# Exist #############################

                                else:
                                    exit()
                        project(name)
                    else:
                        project(name)

        else:
            os.system("clear")
            print("This email isnt valid")

            validatelogin()
