#GUI Python File:
#GUI class is used to develop a graphical user interface using python's gui library import
  # GUI class links all previously created classes into one user interface
  # This class will hold all the python source code for creating the GUI

import sys
from tkinter import * #imports library for GUI application
import sqlite3        #database library

#from clients import clients                   #imports python file with clients class
#from EmployeeClass import Employees           #imports employee class
#from EmployeeDB import EmployeesDatabase      #imports employee database class
#from Database import InventoryDatabase        #imports database for expense
#from income import income                     #imports income class
#from incomeDB import incomeDB                 #imports income database class
from records import records                   #imports python file with records class

#imports for Expenses
from ExpenseDatabase import * #InventoryDatabase  # Import InventoryDatabase class from Database.py
from ExpenseClass import Inventory  # Import Inventory class from ExpenseClass.py
from tkinter.ttk import Treeview
import calendar

class HomeScreen(Frame):   #gui application that builds the agriculture graphical interface
    #This is the constructor for the HomeScreen class
    def __init__(self, main=None):                  #function init that sets itself as self and main as the master branch set to None
        Frame.__init__(self,main)                   #Library function Frame is called to produce the frame and initializing the main page
        self.main = main                            #sets self.main equal to main
        self.initialize_GUI()                       #self is not calling to the <initialize_GUI> function below to set all the buttons and links

    def initialize_GUI(self):
        self.main.title("Ag Tech Management");                            #Sets title of the main page to "what's in the quotes"
        self.pack(fill = BOTH, expand = 2);                               #pack is function in tkinter library to place the title on the main page
        quit_button = Button(self ,text = "quit", command = self.quit);   #creates a quit button that will terminate the program when clicked
        quit_button.place(x = 350,y = 350);                               #place the <quit button at 350 pixels in on the x axis and 350 pixels in on the y>

        Employees_button = Button(self, text = "Employees", command = employee)                 #Employees Button created
        Employees_button.place(x = 20, y = 30);

        #Here, we run a function through another function. The intermediate function is sequence. Since
        #sequence intakes another function, we need to use lambda. This will guarantee that the function is only
        #ran when the button is pressed, and not before
        Expenses_button = Button(self, text = "Expenses", command = lambda: self.sequence(runExpeneseClass(root)))  #This calls on the ExpenseClassGUI file
        Expenses_button.place(x = 20, y = 100);

        Income_button = Button(self, text = "Income", command = lambda: self.sequence(income))                       #Income button created
        Income_button.place(x = 20, y = 170);

        Clients_button = Button(self, text = "Clients", command = clients)                     #Clients button created
        Clients_button.place(x = 20, y = 240);

        Records_button = Button(self, text = "Records", command = self.sequence(run_records_gui_class(root)))                     #Records button created
        Records_button.place(x = 20, y = 310);

        application_menu = Menu(self.main);                                    #application_menu of the main window
        self.main.config(menu = application_menu);

        file = Menu(application_menu);                                         #Creates a file button addition to the menu bar
        application_menu.add_cascade(label = "File", menu = file);              #Creates text <File> and sets the drop down button
        file.add_command(label = "Exit_Program", command = self.quit);          #Adds a command for the <File> drop down button

        edit = Menu(application_menu);                                         #Creates an edit button addition to the menu bar
        application_menu.add_cascade(label = "Edit", menu = edit);
        edit.add_command(label = "test1");
        edit.add_command(label = "test2");

    #This is a helper function that will delete the current widgets of the frame
    def sequence(self, funct):
        for child in self.winfo_children():     #This is the loop that will go through the Frames widgets and delete the children
            child.destroy()
        return funct()

def returnHome():       #Created in order to return to the homescreen from any menu
    for child in root.winfo_children():     #This is the loop that will go through the Frames widgets and delete the children
            child.destroy()
    HomeScreen(root)    #This will run the HomeScreen class

class employee(Frame):                                            #<employee> class created for <employee> page when <employee> button is pressed at the main menu
    def __init__ (self,master = None):
        employees_new_frame = Frame.__init__(self,master);           #Frame initiates the class employee and sets to employee_new_frame
        employees_new_frame = Toplevel(self);                        #Creates upon itself a new top level window which is linked towards the button from the main window above
        employees_new_frame.title("Employees");                      #sets the title of the window
        employees_new_frame.geometry("400x400");                     #sets the size in <pixels> of the window
        #insert code here to create buttons, entries and any feature towards specified page


        #

class Expenses(Frame):

    # Creates the first option menus in the expense window
    def createOptionButtons(self):
        self.master.title("Expenses")

        # Creates the add item to inventory button
        addItem = Button(root, text="Add item to inventory", command=lambda: self.sequence(self.addItem))#addItem(master)))  # This button will send to the user to the add item page
        addItem.place(x = 130, y = 100)

        # Creates the view items in inventory button
        inventoryButton = Button(root, text="View items in inventory", command=lambda: self.sequence(self.viewInveroty))  # This button will send the user to the view inventory page
        inventoryButton.place(x = 130, y = 150)

        # Create the total cost button
        totalCost = Button(root, text="Total Cost", command=lambda: self.sequence(self.viewTotalCost))
        totalCost.place(x = 130, y = 200)

        # Creates the back button
        backButton = Button(root, text="Back", command=returnHome)  # This button will return the user to the main page. Still working on it.
        backButton.place(x = 50, y = 350)

    # Creates the add item to inventory button and entries
    def addItem(self):
        self.master.title("Add new item")  # Changes the title of the page to Add New Item

        # Creates a label called nameOfItems and an entry called itemName
        nameOfItem = Label(root, text="Item Name: ")
        nameOfItem.place(x = 110, y = 100)
        self.itemName = Entry(root)       # This will allow the user to enter the name of the item that they will be adding
        self.itemName.place(x = 190, y = 100)

        # Creates the label called itemTypeLabel and a drop down menu called itemTypeChoice
        itemTypeLabel = Label(root, text = "Item's type: ")
        itemTypeLabel.place(x = 110, y = 160)
        self.itemTypeChoice = StringVar(root)       # This makes itemTypeChoice a permanent String
        self.itemTypeChoice.set("Tree")             # Tree is set to the default string of itemTypeChoice
        typeChoices = OptionMenu(root, self.itemTypeChoice, "Tree", "Animal", "Machine")    # Drop down menu is created and options Tree, Animal, and Machine are added to the menu
        typeChoices.place(x = 190, y = 160)


        backButton = Button(root, text = "Back", command=lambda: self.sequence(self.createOptionButtons))
        backButton.place(x = 50, y = 350)
        # Next button
        nextButton = Button(root, text = "Next", command=self.saveNameAndType) #This button will send the user to the add inventory page
        nextButton.place(x = 350, y = 350)

    # Function that creates a new item object and assigns it a name and the type
    def saveNameAndType(self):
        name = self.itemName.get()
        self.item = Inventory(name)
        itemType = self.itemTypeChoice.get()
        self.item.itemType = itemType
        self.sequence(self.addToInventory)

    # Creates the add to inventory options
    def addToInventory(self):
        self.master.title("Add %s to %s inventory" % (self.item.name, self.item.itemType))

        # This assigns the variables month, day, and year to be value holder for integer values
        # They are also set to be values of the class expenses (by using self) so that they can
        # be used in the function updateDay and SaveDate
        self.month = IntVar(self)
        self.day = IntVar(self)
        self.year = IntVar(self)

        # This trace function is used to keep track of when the selected months and years change. This is
        # done to adjust the days of the month according to the month or the year
        self.month.trace('w', self.updateDay)
        self.year.trace('w', self.updateDay)

        numMonths = self.nums(1, 12)  # Runs the nums function that creates a list from 1 to 12
        numYears = self.nums(2015, 2030)  # Runs the nums function that creates a list from 2015 to 2030

        # This creates the drop down menu and assigns the options is the menu. The day menu is left empty and
        # is assigned in the updateDay function
        self.optionmenu_month = OptionMenu(root, self.month, *numMonths)
        self.optionmenu_day = OptionMenu(root, self.day, '')
        self.optionmenu_year = OptionMenu(root, self.year, *numYears)

        # Sets the default value of the month and year options to 1 and 2015 respectively
        self.month.set(numMonths[0])
        self.year.set(numYears[0])

        self.optionmenu_month.place(x = 100, y = 120)
        self.optionmenu_day.place(x = 150, y = 120)
        self.optionmenu_year.place(x = 200, y = 120)


        datePurchased = Label(root, text = "Date Purchased")
        datePurchased.place(x = 150, y = 95)

        quantityPurchasedLabel = Label(root, text="Amount purchased:")
        quantityPurchasedLabel.place(x = 50, y = 180)
        self.quantityPurchasedEntry = Entry(root, bd=5) # Creates input box for user to insert the amount of items purchased
        self.quantityPurchasedEntry.place(x = 180, y = 180)

        pricePaidLabe = Label(root, text="Price paid for all: ")
        pricePaidLabe.place(x = 50, y = 210)
        self.pricePaidEntry = Entry(root, bd=5) # Creates input box for user to insert the price paid for the item
        self.pricePaidEntry.place(x = 180, y = 210)


        backButton = Button(root, text = "Back", command=lambda: self.sequence(self.addItem))
        backButton.place(x = 50, y = 350)

        nextButton = Button(root, text = "Next", command=self.saveQuanAndPrice)
        nextButton.place(x = 350, y = 350)

    # This function will update the days of the month according to the selected month and year
    def updateDay(self, *args):
        # The .get() will obtain the selected month and year values from the drop down menu above
        month = self.month.get()
        year = self.year.get()

        # Creates a loop which chooses the last day of the month according to the month or the year
        if month == 1 or month  == 3 or month  == 5 or month  == 7 or month  == 8 or month  == 10 or month  == 12:
            lastDay = 31
        elif month  == 4 or month  == 6 or month  == 9 or month  == 11:
            lastDay = 30
        # This elif loop uses the leap year formula at account for leap years
        elif month  == 2:
            if (year % 4) == 0:
                if (year % 100) == 0:
                    if (year % 400) == 0:
                        lastDay = 29
                    else:
                        lastDay = 28
                else:
                    lastDay = 29
            else:
                lastDay = 28

        numDays = self.nums(1,lastDay)

        # Assigns menu to the day drop down menu and deletes all of the options in the menu
        menu = self.optionmenu_day['menu']
        menu.delete(0, 'end')

        # Loop for generating the new day menu
        for day in numDays:
            menu.add_command(label=day, command=lambda d = day: self.day.set(d))
        self.day.set(1)

    # Function that creates the range of numbers for the drop down menu
    def nums(self, numStart, numEnd):
        num = range(numStart, numEnd + 1)
        return num

    # Function that assigns the price and quantity to an item
    def saveQuanAndPrice(self):
        self.item.price = self.pricePaidEntry.get()
        self.item.quantity = self.quantityPurchasedEntry.get()
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
        self.master.title("Confirm %s information" % self.item.name)
        name = Label(root, text="Name of item: ")
        name.place(x = 100, y = 50)
        itemName = Label(root, text=self.item.name)
        itemName.place(x = 100, y = 65)

        type = Label(root, text="%s type: " % self.item.name)
        type.place(x = 100, y = 90)
        itemType = Label(root, text=self.item.itemType)
        itemType.place(x = 100, y = 105)

        quantity = Label(root, text="How many %s were bought?" % self.item.name)
        quantity.place(x = 100, y = 130)
        itemQuantity = Label(root, text=self.item.quantity)
        itemQuantity.place(x = 100, y = 145)

        price = Label(root, text="How much did the %s %s cost?" % (self.item.quantity, self.item.name))
        price.place(x = 100, y = 170)
        itemPrice = Label(root, text=self.item.price)
        itemPrice.place(x = 100, y = 185)

        date = Label(root, text="When were %s bought?" % self.item.name)
        date.place(x = 100, y = 210)
        itemDate = Label(root, text=self.item.purchaseDate)
        itemDate.place(x = 100, y = 225)


        backButton = Button(root, text = "Back", command=lambda: self.sequence(self.addToInventory))
        backButton.place(x = 50, y = 350)

        startOverButton = Button(root, text = "Start Over", command=lambda: self.sequence(self.createOptionButtons))
        startOverButton.place(x = 200, y = 350)

        confirmButton = Button(root, text = "Confirm", command=lambda: self.sequence(self.addToDatabase))
        confirmButton.place(x = 320, y = 350)

    # Adds the item to the database
    def addToDatabase(self):
        self.inventoryDB.insertInvetory(self.item)
        return self.successful()

    # Displays a success message when the item is added
    def successful(self):
        self.master.title("%s was added successfully!" % self.item.name)

        succMessage = Message(root, text = "%s was successfully added to the %s list!" % (self.item.name, self.item.itemType))
        succMessage.place(x = 150, y = 150)

        startOverButton = Button(root, text = "Start Over", command=lambda: self.sequence(self.createOptionButtons))#self.saveNameAndType(itemName)))#(self.saveNameAndType(itemName)))  # (itemName)))# lambda: self.sequence(self.test))  #This button will send the user to the add inventory page
        startOverButton.place(x = 150, y = 350)

    # Used to view the inventory
    def viewInveroty(self):
        # Creates the label called chooseTypeLabel and a drop down menu called chooseItemType
        chooseTypeLabel = Label(root, text = "Item's type: ")
        chooseTypeLabel.place(x = 110, y = 160)
        self.chooseItemType = StringVar(root)       # The drop down menu is created and assigned to chooseItemType
        self.chooseItemType.set("Tree")             # Tree is set to the default option in the drop down menu
        typeChoices = OptionMenu(root, self.chooseItemType, "Tree", "Animal", "Machine", "All")    # Options Tree, Animal, Machine, and ALL are added to the drop down menu
        typeChoices.place(x = 190, y = 160)

        backButton = Button(root, text = "Back", command=lambda: self.sequence(self.createOptionButtons))  # This button will return the user to the expenses option page
        backButton.place(x = 50, y = 350)

        nextButton = Button(root, text = "Next", command=lambda: self.sequence(self.displayGeneralInventory))#self.saveNameAndType(itemName)))#(self.saveNameAndType(itemName)))  # (itemName)))# lambda: self.sequence(self.test))  #This button will send the user to the add inventory page
        nextButton.place(x = 350, y = 350)

    # Used to create the inventory table
    def displayGeneralInventory(self):
        # This creates a table using the function Treeview
        self.tree = Treeview(height="20", columns=("Name", "Current Quantity"))
        self.tree.pack()
        self.tree.heading('#1', text = "Name", anchor = CENTER)
        self.tree.heading('#2', text = "Current Quantity", anchor = CENTER)
        self.tree.column('#1', minwidth=0, width = 100)
        self.tree.column('#2', minwidth=0, width = 100)
        self.tree.column('#0', minwidth=0, width = 0)

        itemType = self.chooseItemType.get()

        if(itemType == "All"):
            self.obtainData("Tree")
            self.obtainData("Animal")
            self.obtainData("Machine")

        else:
            self.obtainData(itemType)

    # Adds database data to the inventory table
    def obtainData(self, type):
        for row in (self.inventoryDB.getOverviewInventory(type)):
            name = row[0]
            totalQuantity = row[1]

            # Inserts data into the table. Each entry is tagged with the name and the type
            # This is done in order to make identifying the entries easier for when detailed
            # tables are requested
            self.tree.insert("", "end", values = (name,totalQuantity), tag= [name, type])

        # Creates a bak function that is used in the displayGeneralInventory functions
        self.backFunction = self.displayGeneralInventory

        # Binds a double click function to the Treeview table. If an entry is double clicked,
        # the function displayGeneralInventory is ran
        self.tree.bind("<Double-1>", self.displayDetailedInventory)

        backButton = Button(root, text="Back", command=lambda: self.sequence(self.viewInveroty))  # This button will return the user to the main page. Still working on it.
        backButton.place(x = 50, y = 350)

    # Creates table when an entry is double clicked
    def displayDetailedInventory(self, event):
        # The selected item's tag are extracted and assigned to name and type
        itemSelected = self.tree.selection()
        name = self.tree.item(itemSelected,"tag")[0]
        type = self.tree.item(itemSelected, "tag")[1]

        for child in root.winfo_children():
            child.destroy()

        self.createDisplayTable()

        self.obtainDetailedData(name, type)

    # Adds detailed database data to the inventory table
    def obtainDetailedData(self,name, type):
        for row in (self.inventoryDB.getDetailedInventory(type, name)):
            name = row[0]
            purchaseDate = row[1]
            Quantity = row[3]
            Price = row[4]
            self.tree.insert("", "end", values = (name,purchaseDate,Quantity, Price))

        backButton = Button(root, text="Back", command=lambda: self.sequence(self.backFunction))
        backButton.place(x = 50, y = 350)

    # Creates the view total cost by month and year buttons
    def viewTotalCost(self):
        viewMonth = Button(root, text="View by month", command=lambda: self.sequence(self.viewByMonth))
        viewMonth.place(x = 120, y = 100)

        viewYear = Button(root, text="View by year", command=lambda: self.sequence(self.viewByYear))
        viewYear.place(x = 120, y = 150)

        backButton = Button(root, text="Back", command=lambda: self.sequence(self.createOptionButtons))#displayGeneralInventory))  # This button will return the user to the main page. Still working on it.
        backButton.place(x = 50, y = 350)

    # Creates the options for the user to select a month and year
    def viewByMonth(self):
        monthLabel = Label(root, text="Month")
        yearLabel = Label(root, text="Year")

        self.month = IntVar(self)
        self.year = IntVar(self)

        numMonths = self.nums(1, 12)
        numYears = self.nums(2015, 2030)

        self.optionmenu_month = OptionMenu(root, self.month, *numMonths)
        self.optionmenu_year = OptionMenu(root, self.year, *numYears)

        self.month.set(numMonths[0])
        self.year.set(numYears[0])

        self.optionmenu_month.place(x = 100, y = 100)
        self.optionmenu_year.place(x = 150, y = 100)

        monthLabel.place(x = 100, y = 140)
        yearLabel.place(x = 150, y = 140)

        backButton = Button(root, text = "Back", command=lambda: self.sequence(self.viewTotalCost))  # This button will return the user to the expenses option page
        backButton.place(x = 50, y = 350)

        nextButton = Button(root, text = "Next", command= self.viewTotalCostMonth)#self.viewTotalCostMonth)#self.saveNameAndType(itemName)))#(self.saveNameAndType(itemName)))  # (itemName)))# lambda: self.sequence(self.test))  #This button will send the user to the add inventory page
        nextButton.place(x = 350, y = 350)

    # Creates database table and inserts the respective values by month and year
    def viewTotalCostMonth(self):
        self.createDisplayTable()

        self.totalPrice = 0
        month = self.month.get()
        year = self.year.get()

        self.lengthMonth = len(str(month))
        self.searchDate = str(month) + "/" + str(year)

        InventoryDB = getDatabaseConnection()
        database = InventoryDB.cursor()

        self.insertData("DetailedTreeInventory", "Tree", database, "Month")
        self.insertData("DetailedAnimalInventory", "Animal", database, "Month")
        self.insertData("DetailedMachineInventory", "Machine", database, "Month")

        InventoryDB.close()

        totalPriceLabel = Label(root, text=("Total price for " + calendar.month_name[month] + " in " + str(year) + " is: " + str(self.totalPrice)))
        totalPriceLabel.place(x = 100, y = 350)

        backButton = Button(root, text = "Back", command=lambda: self.sequence(self.viewByMonth))  # This button will return the user to the expenses option page
        backButton.place(x = 50, y = 350)

    # Creates the option for the user to select the year
    def viewByYear(self):
        yearLabel = Label(root, text="Year")

        self.year = IntVar(self)

        numYears = self.nums(2015, 2030)

        self.optionmenu_year = OptionMenu(root, self.year, *numYears)

        self.year.set(numYears[0])

        self.optionmenu_year.place(x = 100, y = 100)
        yearLabel.place(x = 100, y = 140)


        backButton = Button(root, text = "Back", command=lambda: self.sequence(self.viewTotalCost))  # This button will return the user to the expenses option page
        backButton.place(x = 50, y = 350)

        nextButton = Button(root, text = "Next", command= self.viewTotalCostYear)#self.viewTotalCostMonth)#self.saveNameAndType(itemName)))#(self.saveNameAndType(itemName)))  # (itemName)))# lambda: self.sequence(self.test))  #This button will send the user to the add inventory page
        nextButton.place(x = 350, y = 350)

    # Creates database table and inserts the respective values by year
    def viewTotalCostYear(self):
        self.createDisplayTable()

        self.totalPrice = 0
        year = self.year.get()

        InventoryDB = getDatabaseConnection()
        database = InventoryDB.cursor()

        self.insertData("DetailedTreeInventory", "Tree", database, "Year")
        self.insertData("DetailedAnimalInventory", "Animal", database, "Year")
        self.insertData("DetailedMachineInventory", "Machine", database, "Year")

        totalPriceLabel = Label(root, text="Total price for " + str(year) + " is: " + str(self.totalPrice))
        totalPriceLabel.place(x = 100, y = 350)

        backButton = Button(root, text = "Back", command=lambda: self.sequence(self.viewByYear))  # This button will return the user to the expenses option page
        backButton.place(x = 50, y = 350)

    # Inserts the detailed values into the detailed table
    def insertData(self, table, type, database, yearOrMonth):
        if yearOrMonth == "Year":
            for row in database.execute("SELECT * FROM %s" % table ):
                itemdate = row[1]

                if ( str(self.year.get()) == itemdate[-4:]):
                    name = row[0]
                    purchaseDate = row[1]
                    Quantity = row[3]
                    Price = row[4]

                    self.tree.insert("", "end", values = (name,purchaseDate,Quantity, Price),tag = [name, type] )
                    self.totalPrice = self.totalPrice + Price

                self.backFunction = self.viewTotalCostYear

        else:
            for row in database.execute("SELECT * FROM %s" % table ):
                itemdate = row[1]

                if (self.searchDate == (itemdate[0:self.lengthMonth] + "/" + itemdate[-4:])):
                    name = row[0]
                    purchaseDate = row[1]
                    Quantity = row[3]
                    Price = row[4]

                    self.tree.insert("", "end", values = (name,purchaseDate,Quantity, Price), tag = [name, type])
                    self.totalPrice = self.totalPrice + Price

                self.backFunction = self.viewTotalCostMonth

        # If entry is double clicked, the table will acknoledge the click and display the detailed table
        self.tree.bind("<Double-1>", self.displayDetailedInventory)

    def createDisplayTable(self):
        for child in root.winfo_children():
            child.destroy()

        self.tree = Treeview(height="15", columns=("Name", "Purchase Date", "Quantity", "Price"))#, "Description"))
        self.tree.pack()
        self.tree.heading('#1', text = "Name",          anchor = CENTER)
        self.tree.heading('#2', text = "Purchase Date", anchor = CENTER)
        self.tree.heading('#3', text = "Quantity",      anchor = CENTER)
        self.tree.heading('#4', text = "Price",         anchor = CENTER)
        self.tree.column('#1', minwidth=0, width = 95)
        self.tree.column('#2', minwidth=0, width = 95)
        self.tree.column('#3', minwidth=0, width = 95)
        self.tree.column('#4', minwidth=0, width = 95)
        self.tree.column('#0', minwidth=0, width = 0)




    # This is a helper function that will delete the current widgets of the frame
    def sequence(self, run):
        for child in root.winfo_children():
            child.destroy()
        run()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.place();
        self.inventoryDB = InventoryDatabase()
        # self.inventoryDB.createTable()
        self.createOptionButtons()

def runExpeneseClass():
    Expenses(root)

class income(Frame):                                              #<income> class created for <income> page when <income> button is pressed at the main menu
   def __init__(self,master = None):
        Frame.__init__(self, master)
        #Enter function to be called here
        self.master.title("Income")

        #insert code here to create buttons, entries and any feature towards specified page


        #

class clients(Frame):                                             #<clients> class created for <clients> page when <clients> button is pressed at the main menu
   def __init__(self,master = None):
        Frame.__init__(self, master)
        #Enter function to be called here
        self.master.title("Clients")

        #insert code here to create buttons, entries and any feature towards specified page


        #

def run_records_gui_class(root):  #function that will move towards class records_gui_class
    records_gui_class(root);
    
Records = records(); # places value of records class file into Records
class records_gui_class(Frame):                                              #<records> class created for <records> page when <records> button is pressed at the main menu
    
    Records = records();
    
    def __init__(self, master = None):
        Frame.__init__(self, master);
        self.master.title("Records");
        self.menu();
        
    def sequence(self, funct):
        for child in root.winfo_children():     #This is the loop that will go through the Frames widgets and delete the children
            child.destroy()
        return funct();
    
    def menu(self, master = None): #main menu for the buttons related to each of the different categories: sales, employees, payroll
        self.master.title("Records Menu");
        employees = Button(master, text = "Employees", command = lambda: self.sequence(self.add_employee))
        employees.place(x = 250, y = 50);

        sales = Button(master, text = "Sales Records", command = lambda: self.sequence(self.add_sale))
        sales.place(x = 250, y = 100);
        
        yearly_earnings = Button(master, text = "Comparing Yearly Earningss", command = lambda: self.sequence(self.sales_comparison))
        yearly_earnings.place(x = 250, y = 150);
        
        payroll = Button(master, text = "Payroll Records", command = lambda: self.sequence(self.payroll_page))
        payroll.place(x = 250, y = 200);

    def employee_records_database(self):                 #function to call from records class function that creates an employees records database
        Records.create_database_employees();
        print("Employees Records Database Created");
        
    def destroy_employee_database(self):                 #function call to record's method that deletes employee database
        Records.delete_database('employees')
        print("Database Destroyed-");
        
    def add_employee2(none, idnm, n, pn, jt, e, ye):     #function to call from records class function to add an employee to records
        print("Employee Being Stored...")
        Records.store_employee(idnm, n, pn, jt, e, ye);
        print("Empoyee:", n, "Added");
        
    def add_employee(self, master = None):#Add employee function creates a new frame for all widgets dealing with adding employees etc.
     #Button that will, when called create a database for employees by calling it from the records class
        Frame.__init__(self, master);
        self.master.title("Employees");
        
        new_storage_employees = Button(master, text = "New: Employee Record Database", command = lambda: self.employee_records_database())
        new_storage_employees.place(x = 150, y = 20);#placement of the button on the page

        #Entries for the add_employee button
        label1 = Label(master, text = "Id:");
        label1.place(x = 50, y = 110);
        e1 = Entry(master)
        e1.place(x = 100, y = 110);

        label2 = Label(master, text = "Name:")
        label2.place(x = 50, y = 140); 
        e2 = Entry(master)
        e2.place(x = 100, y = 140);

        label3 = Label(master, text = "Phone#:")
        label3.place(x = 50, y = 170)
        e3 = Entry(master)
        e3.place(x = 100, y = 170);

        label4 = Label(master, text = "Job:")
        label4.place(x = 50, y = 200)
        e4 = Entry(master)
        e4.place(x = 100, y = 200);

        label5 = Label(master, text = "Email:")
        label5.place(x = 50, y = 230)
        e5 = Entry(master)
        e5.place(x = 100, y = 230);

        label6 = Label(master, text = "YearE:")
        label6.place(x = 50, y = 270)
        e6 = Entry(master)
        e6.place(x = 100, y = 270);
        #add employee button
        add_employee = Button(master, text = "Add Employee", command = lambda: self.add_employee2((e1.get()),(e2.get()),(e3.get()),(e4.get()),(e5.get()),(e6.get())));
        add_employee.place(x = 50, y = 80);
        #print and view all the employees in the database
        print_employee_added = Button(master, text = "Employee Added")
        print_employee_added.place(x = 400, y = 200);
        print_employee_added.config(command = lambda: self.Records.view_records_employees());
        #Button for deleting the database
        delete_storage_employees = Button(master, text = "Delete: Employee List", command = lambda: self.destroy_employee_database())
        delete_storage_employees.place(x = 400, y = 300);
        #back button to return to menu
        back_button = Button(master, text = "Back", command = lambda: self.sequence(self.__init__))
        back_button.place(x = 500 , y = 500 );
        
        #
    def create_sales_storage(self):
        Records.create_database_sales();
        print("Database for Sales Created");

    def destroy_sales_storage(self):
        Records.delete_database('sales');
        print("Database Destroyed");
        
    def store_asale(none, sn, st, q, p, tc, y):
        print("storing sale...")
        Records.store_sale(sn, st, q, p, tc, y);
        print("Sale Stored")
        
    def add_sale(self,master = None):#add sale function that represents a frame with all functionalities related to adding sales
        Frame.__init__(self, master);
        self.master.title("Sales Information");
        
        new_storage_sales = Button(master, text = "New: Sales List", command = lambda: self.create_sales_storage());
        new_storage_sales.place(x = 150, y = 50);
        #delete sales database button
        delete_sales_database = Button(master, text = "Delete Sales Database", command = lambda: self.destroy_sales_storage());
        delete_sales_database.place(x = 250, y = 50);
        
        #Labels and Entries for the add_sales button   ## each label/entry represents one data value that enters into the add sale function
        label7 = Label(master, text = "Id:");
        label7.place(x = 50, y = 230);
        e7 = Entry(master)
        e7.place(x = 120, y = 230);

        label8 = Label(master, text = "Type:")
        label8.place(x = 50, y = 260);
        e8 = Entry(master)
        e8.place(x = 120, y = 260);

        label9 = Label(master, text = "Quantity:")
        label9.place(x = 50, y = 290)
        e9 = Entry(master)
        e9.place(x = 120, y = 290);

        label10 = Label(master, text = "Price_Per: $")
        label10.place(x = 50, y = 320)
        e10 = Entry(master)
        e10.place(x = 120, y = 320);

        label11 = Label(master, text = "Cost: $")
        label11.place(x = 50, y = 350)
        e11 = Entry(master)
        e11.place(x = 120, y = 350);

        label12 = Label(master, text = "Year:")
        label12.place(x = 50, y = 380)
        e12 = Entry(master)
        e12.place(x = 120, y = 380);
        
        ##Add_sale button that will take in the desired information and store that information into the sales database
        add_sale = Button(master, text = "Add Sale", command = lambda: self.store_asale((e7.get()),(e8.get()),(e9.get()),(e10.get()),(e11.get()),(e12.get())));
        add_sale.place(x = 50, y = 150);

        view_sales_button = Button(master, text = "View Sales", command = lambda: Records.view_sales_records())
        view_sales_button.place(x = 300, y = 280)

        back_button = Button(master, text = "Back", command = lambda: self.sequence(self.__init__))
        back_button.place(x = 500 , y = 500 );
         
    def sales_comparison(self, master = None):#page to deal with the functionality of sorting and printing values of sales for each year for comparison
        Frame.__init__(self, master);
        self.master.title("Sales Comparison");
        tablenames = [];
        
        database = sqlite3.connect('records_information_sales.db');#Connects to database
        
        database2 = database.cursor();
        table = database2.execute('''SELECT name FROM sqlite_master WHERE type='table' ''');#moves through database schema and searches through table names
        
        for t in table:                #transverses through table from the database
            tablenames.append(t[0]);   #appends information into the tablenames array

        if 'sale' in tablenames: #checks if the database is available or not : by fetching table name and checking if name is in list
            compare_sales = Button(master, text = "Compare Years and Income", command = lambda: Records.compare_sales_records());  #if available commit function 
            compare_sales.place(x = 300, y = 350);
        else:
            messagebox.showinfo("ERROR", "Error Database Not Available")
        #Back button to menu of records page
        back_button = Button(master, text = "Back", command = lambda: self.sequence(self.__init__))
        back_button.place(x = 500 , y = 500 );
        
        database2.close(); # closes database
    
    def create_database_payroll(self):                    #creates database function for payroll
        print('Creating Database...');
        Records.create_database_payroll();
        print('Database Created');

    def destroy_database_payroll(self):                   #destroys/removes the database for payroll
        Records.delete_payroll_database();
        print('Database Deleted');

    def storeEandsalary(self, ne, yp, sa ):               #stores an employee with the salary and year given
        Records.store_employee_with_salary(ne, yp, sa);
        print('Salary/Employee Stored');

    def search_salary_year(self,y):                       #function calls from record's class a search function to search and add up payroll for a year/date given
        Records.print_payroll_from_designated_year(y);
        
    def payroll_page(self, master = None):#payroll page that contains all the widgets and functionalities associated with payroll
        Frame.__init__(self, master);
        self.master.title("Payroll");
        #Button: that creates a new database for payroll (employee with salary information)
        payroll_button_database_create = Button(master, text = "Payroll: Create Database", command = lambda: self.create_database_payroll())
        payroll_button_database_create.place(x = 300, y = 300);

        #Button: deletes database for payroll
        payroll_delete_database = Button(master, text = "Payroll: Delete Database", command = lambda: self.destroy_database_payroll())
        payroll_delete_database.place(x = 300, y = 350);


        #Labels/Entries for input for storeing salary for payroll
        name = Label(master, text = "Employee Name");
        name.place(x = 50, y = 110);
        entry1 = Entry(master)
        entry1.place(x = 150, y = 110);

        year_paid = Label(master, text = "Year For Payment");
        year_paid.place(x = 50, y = 140);
        entry2 = Entry(master)
        entry2.place(x = 150, y = 140);

        salary_amount = Label(master, text = "Salary");
        salary_amount.place(x = 50, y = 170);
        entry3 = Entry(master)
        entry3.place(x = 150, y = 170);
        
        #Button: Store Employee with Salary
        store_salary = Button(master, text = "Store Salary", command = lambda: self.storeEandsalary((entry1.get()),(entry2.get()),(entry3.get())))
        store_salary.place(x = 100, y = 200)

        #label/entry widget for payroll year functionality
        payroll_y = Label(master, text = 'Enter Year:')
        payroll_y.place(x = 250, y = 200);
        entrypayroll = Entry(master);
        entrypayroll.place(x = 350, y = 200);
        
        #Button that will reach functionality to print payroll based on an inserted year
        payroll_year = Button(master, text = "Enter Year", command = lambda: self.search_salary_year(entrypayroll.get()));
        payroll_year.place(x = 250, y = 250);
        
        #Back button to menu of records page
        back_button = Button(master, text = "Back", command = lambda: self.sequence(self.__init__))
        back_button.place(x = 500 , y = 500 );

root = Tk()
root.geometry("400x400")
HomeScreenApp = HomeScreen(root)
HomeScreenApp.mainloop()
