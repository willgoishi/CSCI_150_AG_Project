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
from records import records                   #imports python file with records class

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

root = Tk()
root.geometry("1000x1000")
HomeScreenApp = HomeScreen(root)
HomeScreenApp.mainloop()
