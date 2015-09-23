import sqlite3  #imports sqlite3

def getDatabaseConnection():    #defines a function that will allow the program to connect to the database
    return sqlite3.connect('Inventory.db')  #the database is called Inventory.db

class InventoryDatabase():
    def createTable(self):  #Creates a new database
        InventoryDB = getDatabaseConnection()   #the database is assign to the variable InventoryDB
        inv = InventoryDB.cursor()
        inv.execute('''CREATE TABLE Inventory
                    (Type Text, Name TEXT, PurchaseDate TEXT, DateUsed TEXT, Quantity INTEGER, Price INTEGER)''') #These are the categories of the table
        InventoryDB.commit()    #Saves the changes of the table
        InventoryDB.close()     #Closes the table

    def getAllInventory(self):
        InventoryDB = getDatabaseConnection()
        inv = InventoryDB.cursor()
        return inv.execute('SELECT * FROM Inventory ORDER BY Name') #Returns all of the items in the table organized by name

    def insertInvetory(self, item):
        InventoryDB = getDatabaseConnection()
        inv = InventoryDB.cursor()
        inv.execute('''
            INSERT INTO Inventory (Type, Name, PurchaseDate, DateUsed, Quantity, Price) VALUES (?, ?, ?, ?, ?)''',
            (item.name, item.purchaseDate, item.firstUse, item.quantity, item.price)) #inserts new items to the table
        InventoryDB.commit()
        InventoryDB.close()
