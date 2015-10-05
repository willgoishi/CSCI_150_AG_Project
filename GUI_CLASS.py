#GUI Python File: 
#GUI class is used to develop a graphical user interface using python's gui library import
  # GUI class links all previously created classes into one user interface 
  # This class will hold all the python source code for creating the GUI  
  
import sys
from tkinter import * #imports library for GUI application
import sqlite3        #database library

from clients import clients                   #imports python file with clients class
from EmployeeClass import Employees           #imports employee class
from EmployeeDB import EmployeesDatabase      #imports employee database class
from Database import InventoryDatabase        #imports database for expense
from ExpenseClass import Inventory            #imports inventory class for expenses
from income import income                     #imports income class
from incomeDB import incomeDB                 #imports income database class  
from records import records                   #imports python file with records class

class GUI_APPLICATION():   #gui application that builds the agriculture graphical interface
