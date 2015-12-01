import sys
from tkinter import *
import sqlite3        

from income import income                     
from incomeDB import incomeDB                 

def runIncomeClass(root):
    IncomeGUI(root)

class IncomeGUI(Frame):   
    inDB = incomeDB()

    def createIncome(self):
        addIncome = Button(self, text="Add income", command=lambda: self.sequence(self.addMonth))
        addIncome.pack(fill=X, padx=10, pady=20)

        incomeButton = Button(self, text="View income", command =lambda: self.sequence(self.createViewIncomeButtons))
        incomeButton.pack(fill=X, padx=10, pady=5)

    def addMonth(self):
        monthofIncome = Label(self, text = "Select Month: ")
        monthofIncome.pack()
        self.monthChoice = StringVar(self)
        self.monthChoice.set("")
        Choicesformonth = OptionMenu(self, self.monthChoice, "", "January", "February", "March",
                                     "April", "May", "June", "July", "August", "September",
                                     "October", "November", "December")
        Choicesformonth.pack()

        nextButton = Button(self, text="Next", command=lambda: self.addIncome(self.Choicesformonth))
        backButton = Button(self, text="Back", command=lambda: self.sequence(
            self.createIncome))
        backButton.pack()

    def addIncome(self,monthin):
        month = monthin.get()

        nameofItem = Label(self, text="Item Name: ")
        nameofItem.pack()
        self.itemName = Entry(self)
        self.itemName.pack()

        amountinput = Label(self, text="Amount: ")
        amountinput.pack()
        self.amountnumber = Entry(self)
        self.amountnumber.pack()

        priceinput = Label(self, text="Price: ")
        priceinput.pack()
        self.pricenumber = Entry(self)
        self.pricenumber.pack()

        nextButton = Button(self, text="Next",
                            command=lambda: self.saveDetails(self.itemName, self.amountnumber, self.pricenumber))
        nextButton.pack()
        backButton = Button(self, text="Back", command=lambda: self.sequence(
            self.createIncome))
        backButton.pack()

    def saveDetails(self, namein, amountin, pricein):
        item = namein.get()
        amount = amountin.get()
        price = pricein.get()
        self.sequence(self.confirmation)

    def confirmation(self):

        month = Label(self, text="Month: ")
        month.pack()
        monthin = Label(self, text=self.month)
        monthin.pack()
        
        name = Label(self, text="Name of item: ")
        name.pack()
        itemName = Label(self, text=self.item)
        itemName.pack()

        amount = Label(self, text="Amounts: ")
        amount.pack()
        amountdis = Label(self, text=self.item.amount)
        amountdis.pack()

        price = Label(self, text="Price: ")
        price.pack()
        pricedis = Label(self, text=self.item.price)
        pricedis.pack()        
        

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createIncome()
        self.master.title("Income")
