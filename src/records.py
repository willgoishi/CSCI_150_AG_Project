# Records Python file

#Records
    #1:Records employees and equipment into databases
    #2:Creates a record of sales for each year
    #3:Creates a comparison model so that yearly income can be compared and contrasted
    #4:Tracks the records of employee payroll 
    
    
import sys;
from tkinter import *#imports GUI library
import sqlite3       #imports database library

class records:#Records class that takes information and stores/removes information
    
    def _init_(self, daily, monthly, yearly):
        #

    def create_database_entry():
        database = sqlite3.connect('records_information.db');#connects to database
        c = database.cursor();
        c.execute('''CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT,phone TEXT, job_type TEXT, email TEXT ) ''');
        database.commit();
        database.close();
        
    def drop_data_base():
        c = database.cursor();                 #Drops table created
        c.execute('''DROP TABLE employees'''); #     ........
        database.commit();                     #     ........
        database.close();#closes the database

    def store_employee(id_num, employee_name, phone, job_t, email):#stores employee into database
        database = sqlite3.connect('records_information.db');
        c = database.cursor();

        c.execute('''INSERT INTO employees (id, name, phone, job, email) ''',(id_num, employee_name, phone, job_t, email));
        print("Employee Recorded");
        database.commit(); 
        
        database.close();
        
employees = [];#declares array of employees

def retrieve_data(employees):#retrieves data<employee's information> from database then stores that information into an array
    database = sqlite3.conect('records_information.db');
    c.execute('''SELECT id, name, phone, job, email FROM employees''');
    c = database.cursor();
    employees = c.fetchall();
    return employees;

#def search_for_employee(employees):#
