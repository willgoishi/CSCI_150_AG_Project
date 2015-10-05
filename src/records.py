# Records Python file

#Records
    #1:Records employees and equipment into databases
    #2:Creates a record of sales for each year
    #3:Creates a comparison model so that yearly income can be compared and contrasted
    #4:Tracks the records of employee payroll 
    
    
import sys
from tkinter import *#imports GUI library
import sqlite3       #imports database library

class records:#Records class that takes information and stores/removes information
    
    def _init_(self, daily, monthly, yearly):
        #

    def create_database_employees():
        database = sqlite3.connect('records_information_employees.db');#connects to database employees
        c = database.cursor();
        #Creates table employee that holds all the desired characteristics/ variables
        c.execute('''CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT,phone TEXT, job_type TEXT, email TEXT, year_joined TEXT ) ''');
        database.commit();
        database.close();    #closes database
  
    def create_database_sales():#connects to database sales
        database = sqlite3.connect('records_information_sales.db');#connects to database with sales information
        c = database.cursor();
        #Creates table sale that holds sale records and can be used for further analysis 
        c.execute('''CREATE TABLE sale(id INTEGER PRIMARY KEY, Sale_type TEXT, quantity INTEGER, price_per INTEGER, cost INTEGER, year TEXT ) ''');
        database.commit();
        database.close();    #closes database
        
    def view_sales_records():#Prints out the sales records for each year
        database = sqlite3.connect('records_information_sales.db');
        c = database.cursor();
        print("All Contained Records of Sales in Database: \n")
        database.commit();
        
        for row in database.execute('SELECT * FROM sale ORDER BY id'):#iterates through the database and prints information out row by row
            print(row);                                               #prints row by row as loop is commenced 
        database.close();    #closes database
        
    def view_records_employees():#function to view all employees and their information and prints out information
        database = sqlite3.connect('records_information_employees.db');
        c = database.cursor();
        print("All Recorded Information on Employees:");

        for row in database.execute('SELECT * FROM employees ORDER BY id'):#iterates through database and prints values row by row
            print(row);                                                    #prints row <all data contained in row>
        database.close();    #closes database
        
    def delete_database(table_name):#deletes a database 
        database = sqlite3.connect('records_information_employees.db'); #connects to database with employee info
        database2 = sqlite3.connect('records_information_sales.db');    #connects to database with sales info
        c = database.cursor();                      #Drops table created
        d = database2.cursor();
        
        if table_name == 'employees':               #takes input and checks whether input is a string employee 
            c.execute('''DROP TABLE employees ''');   # executes the process of dropping the table from database
        elif table_name == 'sales':                 #takes input and checks whether input is a string sales
            d.execute('''DROP TABLE sale ''');        #executes process of dropping sale table in database
        
        database.commit();   # commits previous actions above <employee database>
        database2.commit();  # commits previous actions above <sales database>
        database.close();    #closes the database
        database2.close();   #closes second database
        
    def store_employee(id_num, employee_name, phone_num, job_t, email_address, year_joined):#stores employee into database
        database = sqlite3.connect('records_information_employees.db');
        c = database.cursor();
        c.execute('''INSERT INTO employees( id , name , phone , job_type , email, year_joined ) VALUES (?,?,?,?,?,?)''',
                  (id_num, employee_name, phone_num, job_t, email_address, year_joined) );

        database.commit();
        print("Employee Recorded");
        database.close();    #closes database
        
    def store_sale(sale_num, sale_type, quantity, price, total_cost, year ):#stores sale into database 
        database = sqlite3.connect('records_information_sales.db');
        c = database.cursor();
        c.execute(''' INSERT INTO sale(id, Sale_type, quantity, price_per, cost, year) VALUES (?,?,?,?,?,?)''', (sale_num, sale_type, quantity, price, total_cost, year));
        database.commit();    
        database.close();    #closes database

