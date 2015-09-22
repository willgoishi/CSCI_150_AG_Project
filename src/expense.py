#Expense Python File 

import sys
from tkinter import *
import sqlite3        #imports the sqlite database library
class expenses: #Class expenses-deals with all expenses related to costs and storing the cost data
    t = Tk();               #declaring t as a new GUI application
    t.title("Expenses");    #Declares title of the GUI
    #Creates Labels for Entry
    Label1 = Label(text = "Expense Type").grid(row=0);
    Label2 = Label(text = "Quantity").grid(row=1);
    Label3 = Label(text = "Price").grid(row=2);
    #Creates Entry
    entry1 = Entry(bd = 15);
    entry1.grid(row=0, column=1);
    entry2 = Entry(bd = 15);
    entry2.grid(row=1,column=1);
    entry3 = Entry(bd = 15);
    entry3.grid(row=2,column=1);
    #Function to print out the entry <Values>
    def entry_values(d1,d2,d3):#function that prints data that is inputted
        print("Item: %s\n Quantity: %s \n Price: %s" (d1.get(),d2.get(),d3.get()))
        
    Button( text='Quit_Application', command=t.quit).grid(row=5, column=1, sticky=W,pady=4);    #Button created to quit the GUI application
    Button( text='Print_Data', command=entry_values).grid(row=6, column=2, sticky=W, pady=4);   #Button created to print data using entry_function
    
    t.mainloop();#loops 
