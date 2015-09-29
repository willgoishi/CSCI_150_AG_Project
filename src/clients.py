
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
        c.execute('''CREATE TABLE customers
                            (name, company, product, quantity, phone, email)''')

        client_database.commit();
        client_database.close();

    #dropping table
    def drop_database():
        c=client_database.cursor();
        c.execute('''DROP TABLE customers''');
        client_database.commit();
        client_database.close();
    
    #stores client info in database
    def store_client_info(name, company, product, quantity, phone, email):
        client_database = sqlite3.connect('client_data.db');
        c=client_database.cursor();

        c.execute('''INSERT INTO aclient (name, company, phone, email)''',(name, company, phone, email));
        print("Client info entered");
        database.commit();
        database.close();

        customers = [];

        def retrieve_data(customers):
            database = sqlite3.connect('client_data.db');
            c.execute('''SELECT name, company, phone, email FROM customers''');
            c=database.cursor();
            customers=c.fetchall();
            return customers;

        

        
        
