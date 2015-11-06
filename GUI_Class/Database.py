import sqlite3  #imports sqlite3

def getDatabaseConnectionTree():    #defines a function that will allow the program to connect to the database
    return sqlite3.connect('TreeInventory.db')  #the database is called Inventory.db

def getDatabaseConnectionAnimal():    #defines a function that will allow the program to connect to the database
    return sqlite3.connect('AnimalInventory.db')  #the database is called Inventory.db

def getDatabaseConnectionMachine():    #defines a function that will allow the program to connect to the database
    return sqlite3.connect('MachineInventory.db')  #the database is called Inventory.db

class InventoryDatabase():
    #Function that creates the databases that will be used
    def createTable(self):
        def createTreeTable(self):  #Creates database for Tree
            InventoryTreeDB = getDatabaseConnectionTree()   #The database is assign to the variable InventoryTreeDB
            tree = InventoryTreeDB.cursor()
            tree.execute('''CREATE TABLE Inventory
                        (Name TEXT, PurchaseDate TEXT, DateUsed TEXT, Quantity INTEGER, Price INTEGER)''') #These are the categories of the table
            InventoryTreeDB.commit()    #Saves the changes of the table
            InventoryTreeDB.close()     #Closes the table

        def createAnimalTable(self):  #Creates database for Animals
            InventoryAnimalDB = getDatabaseConnectionAnimal()   #The database is assign to the variable InventoryAnimalDB
            animal = InventoryAnimalDB.cursor()
            animal.execute('''CREATE TABLE Inventory
                        (Name TEXT, PurchaseDate TEXT, Quantity INTEGER, Price INTEGER)''') #These are the categories of the table
            InventoryAnimalDB.commit()    #Saves the changes of the table
            InventoryAnimalDB.close()     #Closes the table

        def createMachineTable(self):  #Creates database for Machines
            InventoryMachineDB = getDatabaseConnectionMachine()   #The database is assign to the variable InventoryMachineDB
            machine = InventoryMachineDB.cursor()
            machine.execute('''CREATE TABLE Inventory
                        (Name TEXT, PurchaseDate TEXT, DateUsed TEXT, Quantity INTEGER, Price INTEGER)''') #These are the categories of the table
            InventoryMachineDB.commit()    #Saves the changes of the table
            InventoryMachineDB.close()     #Closes the table

        #These three functions call on the above functions and generate the database
        createTreeTable(self)
        createAnimalTable(self)
        createMachineTable(self)

    #Function that will read the inventory stored in the databases
    def getAllInventory(self, type):
        if type.lower() == "tree":
            InventoryTreeDB = getDatabaseConnectionTree()
            tree = InventoryTreeDB.cursor()
            return tree.execute('SELECT * FROM Inventory ORDER BY Name') #Returns all of the items in the table organized by name

        elif type.lower() == "animal":
            InventoryAnimalDB = getDatabaseConnectionAnimal()
            animal = InventoryAnimalDB.cursor()
            return animal.execute('SELECT * FROM Inventory ORDER BY Name') #Returns all of the items in the table organized by name

        elif type.lower() == "machine":
            InventoryMachineDB = getDatabaseConnectionMachine()
            machine = InventoryMachineDB.cursor()
            return machine.execute('SELECT * FROM Inventory ORDER BY Name') #Returns all of the items in the table organized by name

        else:
            print ("Sorry, catefory not found")
            return '0'

    #Function that will insert the inventory stored in the databases
    def insertInvetory(self, item):

        #The if loops are to check the type of the item so it can be added to the correct category
        if item.itemType.lower() == "tree":
            InventoryTreeDB = getDatabaseConnectionTree()
            tree = InventoryTreeDB.cursor()
            tree.execute('''
                INSERT INTO Inventory (Name, PurchaseDate, DateUsed, Quantity, Price) VALUES (?, ?, ?, ?, ?)''',
                (item.name, item.purchaseDate, item.firstUse, item.quantity, item.price, )) #inserts new items to the table
            InventoryTreeDB.commit()
            InventoryTreeDB.close()

        elif item.itemType.lower() == "animal":
            InventoryAnimalDB = getDatabaseConnectionAnimal()
            animal = InventoryAnimalDB.cursor()
            animal.execute('''
                INSERT INTO Inventory (Name, PurchaseDate, Quantity, Price) VALUES (?, ?, ?, ?)''',
                (item.name, item.purchaseDate, item.quantity, item.price)) #inserts new items to the table
            InventoryAnimalDB.commit()
            InventoryAnimalDB.close()

        elif item.itemType.lower() == "machine":
            InventoryMachineDB = getDatabaseConnectionMachine()
            machine = InventoryTreeDB.cursor()
            machine.execute('''
                INSERT INTO Inventory (Name, PurchaseDate, DateUsed, Quantity, Price) VALUES (?, ?, ?, ?, ?)''',
                (item.name, item.purchaseDate, item.firstUse, item.quantity, item.price)) #inserts new items to the table
            InventoryMachineDB.commit()
            InventoryMachineDB.close()

        else:
            print ("Error! Objects type does not have a database.")
