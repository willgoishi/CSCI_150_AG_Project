
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


    def searchbyprod(searchproduct):
        print("PRODUCT SEARCH:", searchproduct);
        namearray=[];
        prodtest="empty";
        i=0;
        client_database=sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''SELECT name FROM customers''');
        namevar=c.fetchall();
        for row in namevar:
            namearray.append(row[0]);
            length=len(namearray);
        while(i<length):
            c.execute('''SELECT product FROM ''' + namearray[i] +''' ''');
            prodvar=c.fetchone();
            for row in prodvar:
                if row==searchproduct:
                    print(namearray[i]); c.execute('''SELECT product, quantity FROM ''' + namearray[i] + ''' ''');
                    quantvar=c.fetchone();
                    for row in quantvar:
                        print(row);
                    i=i+1;
                else: i=i+1;

        
    def delete_client(delete_name):
        client_database=sqlite3.connect('client_data.db');
        c=client_database.cursor();
        answer=input("ARE YOU SURE YOU WANT TO DELETE CLIENT: " + delete_name + "?\n");
        if(answer == "yes"):
            c.execute('''DELETE FROM customers WHERE name=(?) ''', [delete_name]);
            print("DELETED: ", delete_name, "FROM DATABASE");
            client_database.commit();
            client_database.close();
        else: print("DELETE CANCELLED");


    def delete_product(title, delete_prod):
        client_database=sqlite3.connect('client_data.db');
        c=client_database.cursor();
        answer=input("ARE YOU SURE YOU WANT TO DELETE PRODUCT: " +delete_prod + "?\n");
        if(answer == "yes"):
            c.execute('''DELETE FROM ''' + title +''' WHERE product=(?) ''', [delete_prod]);
            print("PRODUCT:", delete_prod, "DELETED FROM RECORD");
            client_database.commit();
            client_database.close();
        else: print("DELETE CANCELLED");


