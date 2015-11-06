from tkinter import *  # Imports all of the functions from tKinter
from Database import InventoryDatabase  # Import InventoryDatabase class from Database.py
from ExpenseClass import Inventory  # Import Inventory class from ExpenseClass.py
#from HomeScreenGUI import HomeScreen  # Import HomeScreen class from HomeScreenGUI.py


# Transition function from Homescreen to Expenses class
def runExpeneseClass(root):
    Expenses(root)


class Expenses(Frame):
    inventoryDB = InventoryDatabase()

    # Creates the first option menus in the expense window
    def createOptionButtons(self):
        # Creates the add item to inventory button
        addItem = Button(self, text="Add item to inventory", command=lambda: self.sequence(self.addItem))  # This button will send to the user to the add item page
        addItem.pack(fill=X, padx=10, pady=20)

        # Creates the view items in inventory button
        inventoryButton = Button(self, text="View items in inventory", command=lambda: self.sequence(self.createViewInventoryButtons))  # This button will send the user to the view inventory page
        inventoryButton.pack(fill=X, padx=10, pady=5)

        # Creates the back button
        backButton = Button(self, text="Back")  # This button will return the user to the main page. Still working on it.
        backButton.pack(side=BOTTOM)

    # Creates the add item to invetory button and entries
    def addItem(self):
        self.master.title("Add new item")  # Changes the title of the page to Add New Item

        # Creates a label called nameOfItems and an entry called itemName
        nameOfItem = Label(self, text="Item Name: ")
        nameOfItem.pack()
        self.itemName = Entry(self,
                              bd=5)  # This will allow the user to enter the name of the item that they will be adding
        self.itemName.pack()

        # Creates the label called itemTypeLabel and a drop down menu called itemTypeChoice
        itemTypeLabel = Label(self, text="Item's type:")
        itemTypeLabel.pack()
        self.itemTypeChoice = StringVar(self)  # The drop down menu is created and assigned to itemTypeChoice
        self.itemTypeChoice.set("Tree")  # Tree is set to the default option in the drop down menu
        typeChoices = OptionMenu(self, self.itemTypeChoice, "Tree", "Animal",
                                 "Machine")  # Options Tree, Animal, and Machine are added to the drop down menu
        typeChoices.pack()

        # Creates the back and next buttons
        # Back button
        backButton = Button(self, text="Back", command=lambda: self.sequence(
            self.createOptionButtons))  # This button will return the user to the expenses option page
        backButton.pack()
        # Next button
        nextButton = Button(self, text="Next", command=lambda: self.saveNameAndType(
            self.itemName))  # (itemName)))# lambda: self.sequence(self.test))  #This button will send the user to the add inventory page
        nextButton.pack()

    # Function that creates a new item and assigns it a name and the type
    def saveNameAndType(self, itemName):
        name = itemName.get()
        self.item = Inventory(name)
        itemType = self.itemTypeChoice.get()
        self.item.itemType = itemType
        self.sequence(self.addToInventory)

    # Creates the add to invetory buttons
    def addToInventory(self):  # , itemName):
        self.master.title("Add %s to %s inventory" % (self.item.name, self.item.itemType))

        datePurchased = Label(self, text="Date Purchased")
        datePurchased.pack()

        # Create date menu
        self.month = IntVar(self)  # Creates the drop down menu for the month
        numMonths = self.nums(1, 12)  # Runs the nums function that creates a list from 1 to 12
        self.month.set(numMonths[0])  # Initial value

        option = OptionMenu(self, self.month, *numMonths)  # Assigns the numMonths list to the drop down option
        option.pack()

        self.day = IntVar(self)  # Creates the drop down menu for the day

        if [1].count(self.month.get()) == 1:  # Loop for chaning days according to the month
            numDays = self.nums(1, 31)  # Not currently working
        else:
            numDays = self.nums(1, 23)

        self.day.set(numDays[0])  # Initial value

        option = OptionMenu(self, self.day, *numDays)  # Assigns the numDays list to the drop down option
        option.pack()

        self.year = IntVar(self)  # Creates the drop down menu for the year
        numYears = self.nums(2015, 2030)  # Runs the nums function that creates a list from 2015 to 2030
        self.year.set(numYears[0])  # Initial value

        option = OptionMenu(self, self.year, *numYears)  # Assigns the numYears list to the drop down option
        option.pack()
        # End of the create date menu

        quantityPurchasedLabel = Label(self, text="Amount of %s purchased:" % self.item.name)
        quantityPurchasedLabel.pack()
        self.quantityPurchasedEntry = Entry(self, bd=5)
        self.quantityPurchasedEntry.pack()

        pricePaidLabe = Label(self, text="Price paid for all %s" % self.item.name)
        pricePaidLabe.pack()
        self.pricePaidEntry = Entry(self, bd=5)
        self.pricePaidEntry.pack()

        backButton = Button(self, text="Back", command=lambda: self.sequence(self.addItem))
        backButton.pack()

        nextButton = Button(self, text="Next",
                            command=lambda: self.saveQuanAndPrice(self.pricePaidEntry, self.quantityPurchasedEntry))
        nextButton.pack()

    # Function that creates the range of numbers for the drop down menu
    def nums(self, numStart, numEnd):
        num = range(numStart, numEnd + 1)
        return num

    # Function that assigns the price and quantity to an item
    def saveQuanAndPrice(self, price, quantity):
        self.item.price = price.get()
        self.item.quantity = quantity.get()
        self.saveDate()
        self.sequence(self.confirmation)

    # Function that assigns the purchase date to an item
    def saveDate(self):
        self.item.purchaseMonth = self.month.get()
        self.item.purchaseDay = self.day.get()
        self.item.purchaseYear = self.year.get()
        self.item.purchaseDate = ("%s/%s/%s" % (self.item.purchaseMonth, self.item.purchaseDay, self.item.purchaseYear))

    # Function that displays the user inputted information
    def confirmation(self):
        name = Label(self, text="Name of item: ")
        name.pack()
        itemName = Label(self, text=self.item.name)
        itemName.pack()

        type = Label(self, text="%s type" % self.item.itemType)
        type.pack()
        itemType = Label(self, text=self.item.itemType)
        itemType.pack()

        quantity = Label(self, text="How many %s were bought?" % self.item.name)
        quantity.pack()
        itemQuantity = Label(self, text=self.item.quantity)
        itemQuantity.pack()

        price = Label(self, text="How much did the %s %s cost?" % (self.item.quantity, self.item.name))
        price.pack()
        itemPrice = Label(self, text=self.item.price)
        itemPrice.pack()

        date = Label(self, text="When were %s bought?" % self.item.name)
        date.pack()
        itemDate = Label(self, text=self.item.purchaseDate)
        itemDate.pack()

    # This is a helper function that will delete the current widgets of the frame
    def sequence(self, funct):
        for child in self.winfo_children():
            child.destroy()
        funct()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createOptionButtons()
        self.master.title("Expenses")
