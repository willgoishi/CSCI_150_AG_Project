
#Clients on Python
    #Creates client profile -> name, company, phone number, email
        #what they purchase -> what item(s) && quantity
    #Finds trends in their purchases


#clients denotes class  #customer=individual clients

import sys;
from tkinter import*
import sqlite3

class clients:
    
    #create database
    def create_database():
        client_database = sqlite3.connect('client_data.db');
        c = client_database.cursor();
        
        #creating table
        c.execute('''CREATE TABLE customers (ID INT, name TEXT, company TEXT, phone TEXT, email TEXT, product TEXT, quantity TEXT)''')

        client_database.commit();
        client_database.close();

    #delete table
    def delete_database():
        client_database=sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''DROP TABLE customers''');
        client_database.commit();
        client_database.close();
    
    #stores client info in database (add client)
    def store_client_info(ID, name, company, phone, email):
        client_database = sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''INSERT INTO customers (ID ,name, company, phone, email) VALUES(?,?,?,?,?)''',(ID, name, company, phone, email));
        print("Client info entered");
        client_database.commit();
        client_database.close();

        customers = [];

    def retrieve_client_data():
        client_database = sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''SELECT ID, name, company, phone, email FROM customers''');
        customers=c.fetchall();
        return customers;
            
        
    def store_sales_info (ID, name, company, product, quantity):
        client_database = sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''INSERT INTO customers(product, quantity)''', (product, quantity));
        print("purchase info entered");
        client_database.commit();
        client_database.close();
        
        sales = [];

    def retrieve_sales_info (sales):
        client_database=sqlite3.connect('client_data.db');
        c.execute('''Select ID, name, company, phone, email, product, quantity FROM customers''');
        c=client_database.cursor();
        sales=c.fetchall();
        return sales;

    def search (name, company):
        

        
        
