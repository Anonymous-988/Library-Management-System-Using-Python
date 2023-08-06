import os
from DBModule import DBconnector
from ItemModule import Item


# UserInterface class is developed to contain user actions only

class UserInterFace:
    def __init__(self, username, fname, uid):
        self.username = username
        self.fname = fname
        self.uid = uid
        # print(f"{self.username} And {self.fname}")

    def UserMenu(self):
        os.system('cls')
        print(f"Welcome, {self.fname}\n\n")
        print("Select any operation:")
        choices={
            1:"Borrow Item" ,
            2:"Return Item",
            3:"Exit",
        }
        for i in choices.keys(): # Loop to print all Choises and key of choise ! 
            print(f"{i} - {choices[i]}")
        Userinput = int(input("Enter your Choice: "))
        # print(UserMenuSwitch(self, Userinput))
        UserMenuSwitch(self, Userinput)




# Dont have Switch Case support in Python versions below 3.10
# Will be using functions and dcitionary for Switch operations

def UserMenuSwitch(self,num):
    switch = {
        1 : Borrow,
        2 : Return,
        3 : Exit,
        4 : Default
    }
    switch.get(num, switch[4])(self)
    
def Borrow(self):
    DBObj = DBconnector()
    os.system('cls')
    print(f"Welcome, {self.fname}\n\n")
    data = []
    itemtype = input("You want to Borrow book or journal: ").lower()
    if(itemtype == 'book'):
        data = DBObj.selectItems("book")
    elif(itemtype == 'journal'):
        data = DBObj.selectItems("journal")
    else:
        print("Invalid Input")
        Borrow(self)
    
    ObjList = []
    for item in data:
        ObjList.append(Item(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))

    print("Select one of the Actions: ")
    print("1. Search by Title\n2. Search by Author\n3. Search by Genre\n")
    choice = int(input("Enter your choice: "))
    if(choice == 1 ):
        ObjMap = {}
        for obj in ObjList:
            ObjMap[obj.title] = obj
        titleInput = input("Enter Title: ")
        BorrowingObjList = []
        for objTitle in ObjMap.keys():
            if titleInput in objTitle:
                BorrowingObjList.append(ObjMap[objTitle])
        if len(BorrowingObjList) == 0:
            print("No Results Found")
            return ""
        print(f"Avaiable {itemtype} according to choice are: ")
        print("Srno\tTitle\tGenre\tPub. Year\tQuantity")
        i = 1
        for obj in BorrowingObjList:
            print(f"{i}\t{obj.title}\t{obj.genre}\t{obj.pyear}\t{obj.quantity}")
            i+=1
        
        borrowItemSrno = int(input("Select SrNo. that you want to borrow: "))
        # print(BorrowingObjList[borrowItemSrno-1].itemid, BorrowingObjList[borrowItemSrno-1].quantity)
        DBObj.updateItem("Borrow", BorrowingObjList[borrowItemSrno-1].itemid, BorrowingObjList[borrowItemSrno-1].quantity)
        DBObj.logItemAction("Borrow", self.uid, BorrowingObjList[borrowItemSrno-1].itemid)
    elif (choice == 2):
        ObjMap = {}
        for obj in ObjList:
            ObjMap[obj.author] = obj
        authorInput = input("Enter Author: ")
        BorrowingObjList = []
        for objAuthor in ObjMap.keys():
            if authorInput in objAuthor:
                BorrowingObjList.append(ObjMap[objAuthor])
        if len(BorrowingObjList) == 0:
            print("No Results Found")
            return ""
        print(f"Avaiable {itemtype} according to choice are: ")
        print("Srno\tTitle\tGenre\tPub. Year\tQuantity")
        i = 1
        for obj in BorrowingObjList:
            print(f"{i}\t{obj.title}\t{obj.genre}\t{obj.pyear}\t{obj.quantity}")
            i+=1
        
        borrowItemSrno = int(input("Select SrNo. that you want to borrow: "))
        # print(BorrowingObjList[borrowItemSrno-1].itemid, BorrowingObjList[borrowItemSrno-1].quantity)
        DBObj.updateItem("Borrow", BorrowingObjList[borrowItemSrno-1].itemid, BorrowingObjList[borrowItemSrno-1].quantity)
        DBObj.logItemAction("Borrow", self.uid, BorrowingObjList[borrowItemSrno-1].itemid)
    else:
        ObjMap = {}
        for obj in ObjList:
            ObjMap[obj.genre] = obj
        genreInput = input("Enter Genre: ")
        BorrowingObjList = []
        for objGenre in ObjMap.keys():
            if genreInput in objGenre:
                BorrowingObjList.append(ObjMap[objGenre])
        if len(BorrowingObjList) == 0:
            print("No Results Found")
            return ""
        print(f"Avaiable {itemtype} according to choice are: ")
        print("Srno\tTitle\tGenre\tPub. Year\tQuantity")
        i = 1
        for obj in BorrowingObjList:
            print(f"{i}\t{obj.title}\t{obj.genre}\t{obj.pyear}\t{obj.quantity}")
            i+=1
        
        borrowItemSrno = int(input("Select SrNo. that you want to borrow: "))
        # print(BorrowingObjList[borrowItemSrno-1].itemid, BorrowingObjList[borrowItemSrno-1].quantity)
        DBObj.updateItem("Borrow", BorrowingObjList[borrowItemSrno-1].itemid, BorrowingObjList[borrowItemSrno-1].quantity)
        DBObj.logItemAction("Borrow", self.uid, BorrowingObjList[borrowItemSrno-1].itemid)


def Return(self):
    DBObj = DBconnector()
    data = DBObj.selectBorrowedItem(self.uid)
    ObjList = []
    for item in data:
        ObjList.append(Item(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
    
    i = 1
    print("List of Borrowed Items are: ")
    print("Srno\tTitle\tGenre\tCategory\tPub. Year\tQuantity")
    for obj in ObjList:
        print(f"{i}\t{obj.title}\t{obj.genre}\t{obj.itemtype}\t{obj.pyear}\t{obj.quantity}")
        i+=1

    returnItemSrno = int(input("Select SrNo. that you want to borrow: "))
    DBObj.updateItem("Return", ObjList[returnItemSrno-1].itemid, ObjList[returnItemSrno-1].quantity)
    DBObj.updateItemAction(self.uid, ObjList[returnItemSrno-1].itemid)

def Exit():
    print("Thank you for Visiting us, see you soon!!")
    return exit()

def Default():
    print("Invalid Choice")