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

class GUI(Frame):   #gui application that builds the agriculture graphical interface
 def __init__(self,main=None):                    #function init that sets itself as self and main as the master branch set to None
        Frame.__init__(self,main);                   #Library function Frame is called to produce the frame and initializing the main page
        self.main = main;                            #sets self.main equal to main
        self.initialize_GUI();                       #self is not calling to the <initialize_GUI> function below to set all the buttons and links
        
    def initialize_GUI(self):
        self.main.title("Ag Tech Management");                            #Sets title of the main page to "what's in the quotes"
        self.pack(fill = BOTH, expand = 2);                               #pack is function in tkinter library to place the title on the main page
        quit_button = Button(self ,text = "quit", command = self.quit);   #creates a quit button that will terminate the program when clicked
        quit_button.place(x = 350,y = 350);                               #place the <quit button at 350 pixels in on the x axis and 350 pixels in on the y>

        Employees_button = Button(self, text = "Employees", command = employee)                 #Employees Button created
        Employees_button.place(x = 20, y = 30);
        
        Expenses_button = Button(self, text = "Expenses", command = expenses)                   #Expenses button created
        Expenses_button.place(x = 20, y = 100);
        
        Income_button = Button(self, text = "Income", command = income)                       #Income button created
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
        expenses_new_frame = Frame.__init__(self,master);
        expenses_new_frame = Toplevel(self);
        expenses_new_frame.title("Expenses");
        expenses_new_frame.geometry("400x400");
        #insert code here to create buttons, entries and any feature towards specified page


        #
        
class income(Frame):                                              #<income> class created for <income> page when <income> button is pressed at the main menu
    def __init__(self,master = None):
        income_new_frame = Frame.__init__(self,master);
        income_new_frame = Toplevel(self);
        income_new_frame.title("Income");
        income_new_frame.geometry("400x400");
        #insert code here to create buttons, entries and any feature towards specified page


        #

class clients(Frame):                                             #<clients> class created for <clients> page when <clients> button is pressed at the main menu
    def __init__(self,master = None):
        clients_new_frame = Frame.__init__(self,master);
        clients_new_frame = Toplevel(self);
        clients_new_frame.title("Clients");
        clients_new_frame.geometry("400x400");
        #insert code here to create buttons, entries and any feature towards specified page


        #

class records(Frame):                                             #<records> class created for <records> page when <records> button is pressed at the main menu
    def __init__(self,master = None):
        records_new_frame = Frame.__init__(self,master);
        records_new_frame = Toplevel(self);
        records_new_frame.title("Records");
        records_new_frame.geometry("1000x1000");

        #Button that will, when called create a database for employees by calling it from the records class
        new_storage_employees = Button(records_new_frame, text = "New: Employee List", command = records.create_database_employees)
        new_storage_employees.place(x = 150, y = 20);#placement of the button on the page

        new_storage_employees = Button(records_new_frame, text = "New: Sales List")
        new_storage_employees.place(x = 150, y = 50);

        add_employee = Button(records_new_frame, text = "Add Employee")
        add_employee.place(x = 50, y = 80);
        
        #Entries for the add_employee button
        label1 = Label(records_new_frame, text = "Id:");
        label1.place(x = 50, y = 110);
        e1 = Entry(records_new_frame)
        e1.place(x = 100, y = 110);
        
        label2 = Label(records_new_frame, text = "Name:")
        label2.place(x = 50, y = 140);
        e2 = Entry(records_new_frame)
        e2.place(x = 100, y = 140);

        label3 = Label(records_new_frame, text = "Phone#:")
        label3.place(x = 50, y = 170)
        e3 = Entry(records_new_frame)
        e3.place(x = 100, y = 170);

        label4 = Label(records_new_frame, text = "Job:")
        label4.place(x = 50, y = 200)
        e4 = Entry(records_new_frame)
        e4.place(x = 100, y = 200);

        label5 = Label(records_new_frame, text = "Email:")
        label5.place(x = 50, y = 230)
        e5 = Entry(records_new_frame)
        e5.place(x = 100, y = 230);

        label6 = Label(records_new_frame, text = "YearE:")
        label6.place(x = 50, y = 270)
        e6 = Entry(records_new_frame)
        e6.place(x = 100, y = 270);
        #
        
        #Add_sale button that will take in the desired information and store that information into the sales database
        add_sale = Button(records_new_frame, text = "Add Sale")
        add_sale.place(x = 50, y = 400);
        #Entries for the add_sales button
        label7 = Label(records_new_frame, text = "Id:");
        label7.place(x = 50, y = 430);
        e7 = Entry(records_new_frame)
        e7.place(x = 120, y = 430);
        
        label8 = Label(records_new_frame, text = "Type:")
        label8.place(x = 50, y = 460);
        e8 = Entry(records_new_frame)
        e8.place(x = 120, y = 460);

        label9 = Label(records_new_frame, text = "Quantity:")
        label9.place(x = 50, y = 490)
        e9 = Entry(records_new_frame)
        e9.place(x = 120, y = 490);

        label10 = Label(records_new_frame, text = "Job:")
        label10.place(x = 50, y = 520)
        e10 = Entry(records_new_frame)
        e10.place(x = 120, y = 520);

        label11 = Label(records_new_frame, text = "Price_Per: $")
        label11.place(x = 50, y = 550)
        e11 = Entry(records_new_frame)
        e11.place(x = 120, y = 550);

        label12 = Label(records_new_frame, text = "Cost: $")
        label12.place(x = 50, y = 580)
        e12 = Entry(records_new_frame)
        e12.place(x = 120, y = 580);

        label13 = Label(records_new_frame, text = "Year:")
        label13.place(x = 50, y = 610)
        e13 = Entry(records_new_frame)
        e13.place(x = 120, y = 610);
        #
        delete_storage_employees = Button(records_new_frame, text = "Delete: Employee List")#, command = records.delete_database('employees'))
        delete_storage_employees.place(x = 700, y = 150);

        delete_storage_sales = Button(records_new_frame, text = "Delete: Sales List")#, command = records.delete_database('sales'))
        delete_storage_sales.place(x = 700, y = 180);
        
        view_employees_button = Button(records_new_frame, text = "View Employees", command = records.view_records_employees)
        view_employees_button.place(x = 700, y = 250);

        view_sales_button = Button(records_new_frame, text = "View Sales", command = records.view_sales_records)
        view_sales_button.place(x = 700, y = 280)

        compare_sales = Button(records_new_frame, text = "Compare Years and Income", command = records.compare_sales_records)
        compare_sales.place(x = 700, y = 350);

root = Tk()
root.geometry("400x400")
my_gui = GUI(root)
root.mainloop()

