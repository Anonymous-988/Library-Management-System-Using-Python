from UserModule import User
from UserInterfaceModule import UserInterFace
import os,time

# Prints User Menu
def UserMenu():
    os.system('cls')
    print("Library Management System\n\n")
    choices={
        1:"User Login" ,
        2:"User Registeration",
        3:"Admin login",
        4:"Exit"
    }
    for i in choices.keys(): # Loop to print all Choises and key of choise ! 
        print(f"{i} - {choices[i]}")
    Userinput = int(input("Enter your Choice: "))
    UserSwitch(Userinput)


# USer to enact Switch Case
def UserSwitch(num):
    switch = {
        1 : UserLogin,
        2 : UserRegister,
        3 : AdminLogin,
        4 : Exit,
        5 : Default
    }
    switch.get(num, switch[5])()

def UserLogin():
    os.system('cls')
    print("User Login Page\n\n")
    userObj = User()
    if(userObj.LoginUser()):
        print("Login Successfull")
        time.sleep(2)
        UIobj = UserInterFace(userObj.username, userObj.fname, userObj.uid)
        UIobj.UserMenu()

    else:
        print("Username or Password is incorrect")
 
def UserRegister():
    os.system('cls')
    print("User Registeration Page\n\n")
    userObj = User()
    if(userObj.CreateUser()):
        UserLogin()
    else:
        UserRegister()


# Added to implement Admin Controls to application
# Can be used to update catalogue and remove unwanted users
# Need introduce AdminModule incase Admins controls are needed
def AdminLogin():
    os.system('cls')
    print("Admin Login Page\n\n")
    userObj = User()
    if(userObj.LoginUser()):
        print("Admin Loggged in")
    else:
        print("Username or Password is incorrect")

def Exit():
    print("Thank you for Visiting us, see you soon!!")
    return exit()

def Default():
    print("Invalid Choice")
    UserMenu()

# Entry point to application
if __name__ == "__main__":
    UserMenu()