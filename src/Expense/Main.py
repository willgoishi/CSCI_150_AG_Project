from Database import InventoryDatabase  #Import InventoryDatabase class from Database.py
from ExpenseClass import Inventory      #Import Inventory class from ExpenseClass.py

inventoryDB = InventoryDatabase()   #Make a new object from the InventoryDatabase class and call it inventoryDB
inventoryDB.createTable()           #Create a table in the database

itemType     = str(raw_input("What type is the item (i.e. Tree, Animal, Machine...)? "))    #Gets item type
itemName     = str(raw_input("What item is being added? "))                                 #Gets item name


item = Inventory(itemName)      #Assign item to a new object in the inventory class with the appropriate name
item.itemType     = itemType

if (itemType == 'Tree'):   #Checks to see if the type of the item is Tree
    item.quantity      = int(raw_input(("How many pounds of %s were bought? ") % (itemName)))
    item.price         = int(raw_input(("How much did %d pounds of %r cost? ") % (item.quantity, itemName)))
    item.purchaseDay   = int(raw_input(("What day was %s bought? ") % (item.quantity, itemName)))
    item.purchaseMonth = int(raw_input(("What month was %s bought? ") % (item.quantity, itemName)))
    item.purchaseYear  = int(raw_input(("What year was %s bought? ") % (item.quantity, itemName)))
    item.purchaseDate  = (("%d/%d/%d") % (item.purchaseMonth, item.purchaseDay, item.purchaseYear)
    item.firstUse      = '01/05/2015'
    item.lastUse       = '01/12/2015'

elif (itemType == 'Animal'):    #Checks to see if the type of the item is Animal
    item.quantity      = int(raw_input(("How many %s were bought? ")           % (itemName)))
    item.price         = int(raw_input(("How much did %d %r cost? ")           % (item.quantity, itemName)))
    item.purchaseDay   = int(raw_input(("How much did %d pounds of %r cost? ") % (item.quantity, itemName)))
    item.purchaseMonth = int(raw_input(("How much did %d pounds of %r cost? ") % (item.quantity, itemName)))
    item.purchaseYear  = int(raw_input(("How much did %d pounds of %r cost? ") % (item.quantity, itemName)))
    item.purchaseDate  = (("%d/%d/%d") % (item.purchaseMonth, item.purchaseDay, item.purchaseYear)

elif (itemType == 'Machine'):   #Checks to see if the type of the item is Machine
    item.quantity      = int(raw_input(("How many %s were bought? ")           % (itemName)))
    item.price         = int(raw_input(("How much did %d %r cost? ")           % (item.quantity, itemName)))
    item.purchaseDay   = int(raw_input(("How much did %d pounds of %r cost? ") % (item.quantity, itemName)))
    item.purchaseMonth = int(raw_input(("How much did %d pounds of %r cost? ") % (item.quantity, itemName)))
    item.purchaseYear  = int(raw_input(("How much did %d pounds of %r cost? ") % (item.quantity, itemName)))
    item.purchaseDate  = (("%d/%d/%d") % (item.purchaseMonth, item.purchaseDay, item.purchaseYear)

inventoryDB.insertInvetory(item)    #Runs the insertInventory function from Database.py

for inventory in inventoryDB.getAllInventory(): #Runs the getAllInventory function from Database.py to print the table
    print inventory
