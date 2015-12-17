import sys
from tkinter import * #imports library for GUI application
import sqlite3        #database library

from income import *                     #imports income class
from incomeDB import *                 #imports income database class
from testGUI import *
from tkinter.ttk import Treeview
import calendar

def runIncomeClass(root):
    IncomeGUI(root)

class IncomeGUI(Frame):   
    inDB = incomeDB()

    def createIncome(self):
        addIncome = Button(self, text="Add income", command=lambda: self.sequence(self.addMonth))
        addIncome.pack(fill=X, padx=10, pady=20)

        incomeButton = Button(self, text="View income", command =lambda: self.sequence(self.viewIncome))
        incomeButton.pack(fill=X, padx=10, pady=5)

        backButton = Button(self, text="Back")
        backButton.pack(side=BOTTOM)

    def addMonth(self):
        monthlabel = Label(self, text = "Select Month: ")
        monthlabel.pack()
        self.monthChoice = IntVar(self)
        months = self.numberings(1, 12)
        self.monthChoice.set(1) 
        self.monthInput = OptionMenu(self, self.monthChoice, *months)
        self.monthInput.pack()
        yearlabel = Label(self, text = "Select Year: ")
        yearlabel.pack()
        self.yearChoice = IntVar(self)
        years = self.numberings(2000, 2020)
        self.yearChoice.set(2000) 
        self.yearInput = OptionMenu(self, self.yearChoice, *years)
        self.yearInput.pack()
        

        nextButton = Button(self, text="Next", command=lambda: self.sequence(self.addIncome))
        nextButton.pack()
        backButton = Button(self, text="Back", command=lambda: self.sequence(
            self.createIncome))
        backButton.pack()

    def addIncome(self):
        month = self.monthChoice.get()
        self.income = income(month)
        self.income.year = self.yearChoice.get()

        amountlabel = Label(self, text="Amount of items sold this month: ")
        amountlabel.pack()
        self.amountinput = Entry(self)
        self.amountinput.pack()

        incomelabel = Label(self, text="Income earned: ")
        incomelabel.pack()
        self.incomeinput = Entry(self)
        self.incomeinput.pack()

        nextButton = Button(self, text="Next",
                            command= self.saveDetails)
        nextButton.pack()
        backButton = Button(self, text="Back", command=lambda: self.sequence(
            self.createIncome))
        backButton.pack()

    def saveDetails(self):
        self.income.amount = self.amountinput.get()
        self.income.income = self.incomeinput.get()
        self.sequence(self.confirmation)

    def confirmation(self):

        year = Label(self, text="Year: ")
        year.pack()
        yearin = Label(self, text=self.income.year)
        yearin.pack()

        month = Label(self, text="Month: ")
        month.pack()
        monthin = Label(self, text=self.income.month)
        monthin.pack()

        quantity = Label(self, text="Amount of items sold this month: ")
        quantity.pack()
        itemQuantity = Label(self, text=self.income.amount)
        itemQuantity.pack()

        price = Label(self, text="Income earned: ")
        price.pack()
        itemPrice = Label(self, text=self.income.income)
        itemPrice.pack()        

        nextButton = Button(self, text="Next",
                            command=lambda: self.sequence(self.addToIncomeDatabase))
        nextButton.pack()
        backButton = Button(self, text="Back", command=lambda: self.sequence(
            self.createIncome))
        backButton.pack()

    def addToIncomeDatabase(self):
        self.incomeDB.insertIntoDB(self.income)

        addedMessage = Message(self, text = "Added to database!")
        addedMessage.pack()

        endSessionButton = Button(self, text = "End Session", command=lambda: self.sequence(self.createIncome))
        endSessionButton.pack()

    def viewIncome(self):
        self.tree = Treeview(height="20", columns=("Year", "Month", "Income"))
        self.tree.pack()
        self.tree.heading('#1', text = "Year", anchor = CENTER)
        self.tree.heading('#2', text = "Month", anchor = CENTER)
        self.tree.heading('#3', text = "Income", anchor = CENTER)
        self.tree.column('#1', minwidth=0, width = 100)
        self.tree.column('#2', minwidth=0, width = 100)
        self.tree.column('#3', minwidth=0, width = 100)
        self.tree.column('#0', minwidth=0, width = 0)

        for row in (self.incomeDB.getInfo()):
            year = row[1]
            month = row[0]
            income = row[3]

            self.tree.insert("", "end", values = (year,month,income))

        backButton = Button(self, text="Back", command=lambda: self.sequence(
            self.createIncome))
        backButton.pack()
        

    def sequence(self, funct):
        for child in self.winfo_children():
            child.destroy()
        funct()

    def numberings(self, first, last):
        num = range(first, last + 1)
        return num

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createIncome()
        self.incomeDB = incomeDB()
        #self.incomeDB.createDB()
        self.master.title("Income")
