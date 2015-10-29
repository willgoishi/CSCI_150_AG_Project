
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
        c.execute('''CREATE TABLE customers (ID INT, name TEXT, phone TEXT, email TEXT)''')
        client_database.commit();
        client_database.close();

    #delete table
    def delete_database():
        client_database=sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''DROP TABLE customers''');
        client_database.commit();
        client_database.close();
    
    def delete_table(choice):
        client_database=sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''DROP TABLE ''' + choice + ''' ''');
        client_database.commit();
        client_database.close();
    
    #stores client info in database (add client)
    #stores client info in database (add client)
    def store_client_info(ID, name, phone, email):
        client_database = sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''INSERT INTO customers (ID ,name, phone, email) VALUES(?,?,?,?)''',(ID, name, phone, email));
        print("CLIENT INFO ENTERED:", name);
        c.execute('''CREATE TABLE '''+ name +'''(product TEXT, quantity INT)''')
        print("PURCHASE TABLE CREATED:", name);
        client_database.commit();
        client_database.close();

        customers = [];

    def retrieve_client_data():
        client_database = sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''SELECT ID, name, phone, email FROM customers''');
        customers=c.fetchall();
        print("RETRIEVING CLIENT DATA:");
        for row in customers: print(row);
        return customers;
            
        
          
    def store_sales_info (name, product, quantity):
        client_database = sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''INSERT INTO ''' + name+ '''(product, quantity) VALUES(?,?)''',(product, quantity));
        print("PURCHASE INFO ENTERED:", name);
        client_database.commit();
        client_database.close();
        
        sales = [];
        
    def retrieve_sales_info (choice):
        client_database=sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''SELECT product, quantity FROM ''' + choice +''' ''');
        sales=c.fetchall();
        print("RETRIEVING SALES INFO:", choice);
        for row in sales: print(row);
        return sales;


    def retrieve_one_client(n):
        print("RETRIEVING ONE CLIENT:", n);
        client_database=sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''SELECT ID, name, phone, email FROM customers WHERE name=(?) ''', [n]);
        searchvar=c.fetchall();
        for row in searchvar:
            print(row);
    
    def search(searchname):
        namearray=[];
        client_database=sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''SELECT ID, name, phone, email FROM customers''');
        searchvar=c.fetchall();
        for row in searchvar:
            namearray.append(row[1]);
        i=0;
        length=len(namearray);
        while(i<length):
            if(namearray[i]==searchname):
                print("SEARCH FOUND:", namearray[i]);
                c.execute('''SELECT ID, name, phone, email FROM customers WHERE name=(?) ''', [namearray[i]]);
                searchvar=c.fetchall();
                for row in searchvar:
                    print(row);
                c.execute('''SELECT product, quantity FROM ''' + namearray[i] +''' ''');
                sales=c.fetchall();
                for row in sales:
                    print(row);
                i=i+1;
            else: i=i+1;



        
        
