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
from ExpenseClassGUI import runExpeneseClass   #imports runExpeneseClass from ExpenseClassGUI
#from income import income                     #imports income class
#from incomeDB import incomeDB                 #imports income database class
#from records import records                   #imports python file with records class

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

        Records_button = Button(self, text = "Records", command = records)                     #Records button created
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



class employee(Frame):                                            #<employee> class created for <employee> page when <employee> button is pressed at the main menu
    def __init__ (self,master = None):
        employees_new_frame = Frame.__init__(self,master);           #Frame initiates the class employee and sets to employee_new_frame
        employees_new_frame = Toplevel(self);                        #Creates upon itself a new top level window which is linked towards the button from the main window above
        employees_new_frame.title("Employees");                      #sets the title of the window
        employees_new_frame.geometry("400x400");                     #sets the size in <pixels> of the window
        #insert code here to create buttons, entries and any feature towards specified page


        #

class expenses(Frame):                                            #<expenses> class created for <expenses> page when <expenses> button is pressed at the main menu
    def __init__(self,master = None):
        Frame.__init__(self, master)
        #Enter function to be called here
        self.master.title("Expenses")

        #insert code here to create buttons, entries and any feature towards specified page


        #

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

class records(Frame):                                             #<records> class created for <records> page when <records> button is pressed at the main menu
    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.master.title("Clients")

        #Button that will, when called create a database for employees by calling it from the records class
        new_storage_employees = Button(self, text = "New: Employee List", command = records.create_database_employees)
        new_storage_employees.place(x = 150, y = 20);#placement of the button on the page

        new_storage_employees = Button(self, text = "New: Sales List")
        new_storage_employees.place(x = 150, y = 50);

        add_employee = Button(self, text = "Add Employee")
        add_employee.place(x = 50, y = 80);

        #Entries for the add_employee button
        label1 = Label(self, text = "Id:");
        label1.place(x = 50, y = 110);
        e1 = Entry(self)
        e1.place(x = 100, y = 110);

        label2 = Label(self, text = "Name:")
        label2.place(x = 50, y = 140);
        e2 = Entry(self)
        e2.place(x = 100, y = 140);

        label3 = Label(self, text = "Phone#:")
        label3.place(x = 50, y = 170)
        e3 = Entry(self)
        e3.place(x = 100, y = 170);

        label4 = Label(self, text = "Job:")
        label4.place(x = 50, y = 200)
        e4 = Entry(self)
        e4.place(x = 100, y = 200);

        label5 = Label(self, text = "Email:")
        label5.place(x = 50, y = 230)
        e5 = Entry(self)
        e5.place(x = 100, y = 230);

        label6 = Label(self, text = "YearE:")
        label6.place(x = 50, y = 270)
        e6 = Entry(self)
        e6.place(x = 100, y = 270);
        #

        #Add_sale button that will take in the desired information and store that information into the sales database
        add_sale = Button(self, text = "Add Sale")
        add_sale.place(x = 50, y = 400);
        #Entries for the add_sales button
        label7 = Label(self, text = "Id:");
        label7.place(x = 50, y = 430);
        e7 = Entry(self)
        e7.place(x = 120, y = 430);

        label8 = Label(self, text = "Type:")
        label8.place(x = 50, y = 460);
        e8 = Entry(self)
        e8.place(x = 120, y = 460);

        label9 = Label(self, text = "Quantity:")
        label9.place(x = 50, y = 490)
        e9 = Entry(self)
        e9.place(x = 120, y = 490);

        label10 = Label(self, text = "Job:")
        label10.place(x = 50, y = 520)
        e10 = Entry(self)
        e10.place(x = 120, y = 520);

        label11 = Label(self, text = "Price_Per: $")
        label11.place(x = 50, y = 550)
        e11 = Entry(self)
        e11.place(x = 120, y = 550);

        label12 = Label(self, text = "Cost: $")
        label12.place(x = 50, y = 580)
        e12 = Entry(self)
        e12.place(x = 120, y = 580);

        label13 = Label(self, text = "Year:")
        label13.place(x = 50, y = 610)
        e13 = Entry(self)
        e13.place(x = 120, y = 610);
        #
        delete_storage_employees = Button(self, text = "Delete: Employee List")#, command = records.delete_database('employees'))
        delete_storage_employees.place(x = 700, y = 150);

        delete_storage_sales = Button(self, text = "Delete: Sales List")#, command = records.delete_database('sales'))
        delete_storage_sales.place(x = 700, y = 180);

        view_employees_button = Button(self, text = "View Employees", command = records.view_records_employees)
        view_employees_button.place(x = 700, y = 250);

        view_sales_button = Button(self, text = "View Sales", command = records.view_sales_records)
        view_sales_button.place(x = 700, y = 280)

        compare_sales = Button(self, text = "Compare Years and Income", command = records.compare_sales_records)
        compare_sales.place(x = 700, y = 350);

root = Tk()
root.geometry("400x400")
HomeScreenApp = HomeScreen(root)
HomeScreenApp.mainloop()
