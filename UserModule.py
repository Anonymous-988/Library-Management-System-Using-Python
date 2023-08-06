from DBModule import DBconnector

# User class is used to initialise user object.
# It is used as a session object for the user.

class User:
    def __init__(self):
        self.uid = ""
        self.fname = ""
        self.lname = ""
        self.username = ""
        self.password = ""


    def CreateUser(self):
        self.fname = input("Enter your FirstName: ")
        self.lname = input("Enter your LastName: ")
        self.username = input("Enter your Username: ")
        self.password = input("Enter your Password: ")

        obj = DBconnector()
        try:
            obj.insertUser(self.fname, self.lname, self.username, self.password)
        except:
            print("User Already Exist")
            return 0
        else:
            print(f"User({self.username}) Registered Successfully")
            return 1

    def LoginUser(self):
        self.username = input("Enter your Username: ")
        self.password = input("Enter your Password: ")

        obj = DBconnector()
        try:
            data = obj.selectUser(self.username)
            # print(data[4])
            # print(f"Password: {password}")
            # print(f"Self.Password: {self.password}")
            if(data[4] != self.password):
                return 0
        except Exception as e:
            # print(e)
            return 0
        else:
            self.uid = data[0]
            self.fname = data[1]
            self.uname = data[2]
            return 1
        
    def LoginAdmin(self):
        self.username = input("Enter your Username: ")
        self.password = input("Enter your Password: ")

        obj = DBconnector()
        try:
            if(self.username != "admin"):
                return 0 
            data = obj.selectUser("admin")
            # print(data[4])
            # print(f"Password: {password}")
            # print(f"Self.Password: {self.password}")
            if(data[4] != self.password):
                return 0
        except Exception as e:
            # print(e)
            return 0
        else:
            self.uid = data[0]
            self.fname = data[1]
            self.uname = data[2]
            return 1
