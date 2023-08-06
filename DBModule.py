import mysql.connector


# DBConnector is the class used to contain database operation
# DBConnector will be used throughout application.

class DBconnector:
    def updateItemAction(self, uid, itemid):
        review = input("Please provide your reviews: ")
        rating = 0
        while True:
            rating = int(input("Please provide Rating between(1-5):"))
            if rating>0 and rating<6:
                break;
        
            
        sql = f"update user_action set action='Return', review='{review}', rating={rating} where itemid={itemid} and uid={uid}"
        self.DBhandler.execute(sql)
        self.mydb.commit()
        print("Updated Borrowed Item")
        return ""

    def selectBorrowedItem(self, uid):
        self.DBhandler.execute(f"select * from items,user_action where user_action.itemid=items.itemid and uid={uid} order by aid")
        data = self.DBhandler.fetchall()
        return data

    def logItemAction(self, action, uid, itemid):
        sql = "INSERT INTO user_action (action, uid, itemid) VALUES (%s, %s, %s)"
        val = (action, uid, itemid)
        self.DBhandler.execute(sql,val)
        self.mydb.commit()
        print("Action Logged")
        return "Action Logged"

    def updateItem(self, action, itemid, quantity):
        if(action == "Borrow"):
            quantity-=1
            self.DBhandler.execute(f"update items set quantity={quantity} where itemid={itemid}")
            self.mydb.commit()
            print("Updated Borrowed Item")
        else:
            quantity+=1
            self.DBhandler.execute(f"update items set quantity={quantity} where itemid={itemid}")
            self.mydb.commit()
            print("Updated Returned Item")
            

    def selectItems(self, itemtype):
        self.DBhandler.execute(f"select * from items where itemtype='{itemtype}' and quantity>0")
        data = self.DBhandler.fetchall()
        return data

    def selectUser(self, username):
        self.DBhandler.execute(f"select * from users where email='{username}'")
        data = self.DBhandler.fetchone()
        # print(data)
        return data
    
    def selectAdmin(self):
        self.DBhandler.execute(f"select password from users where email='admin'")
        data = self.DBhandler.fetchone()
        # print(data)
        return data[0]

    def insertUser(self, fname, lname, userName, passWord):
        sql = "INSERT INTO users (fname, lname, email, password) VALUES (%s, %s, %s, %s)"
        val = (fname, lname, userName, passWord)
        self.DBhandler.execute(sql,val)

        self.mydb.commit()

        print(self.DBhandler.rowcount, "record inserted.")
    
    def __init__(self):
        self.host="localhost"
        self.user="root"
        self.password=""
        self.database="library"

        self.mydb = mysql.connector.connect(
            host= self.host,
            user= self.user,
            password= self.password,
            database= self.database
        )

        self.DBhandler = self.mydb.cursor()
