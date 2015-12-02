#IMPORTANT: NEW CLIENTS CODE -> SOME SYNTAX IN ORIGINAL COULD NOT BE READ BY TKINTER -> ISSUE FOUND ON 11/17/15
#UPLOADED TO GITHUB ON: 11/29/15
#12/2/15 -> REMOVED PRINTS THAT WERE BEING USED TO TEST EXECUTION (TO SPEED UP EXECUTION TIME w/ GUI) && FIXED SEARCH BY NAME ERROR WHERE IF NAME DIDNT EXIST IN SALES DATABASE, WOULD RETURN ERROR && FEW MINOR CHANGES


#Clients
#Creates client profile DB -> ID, name, phone number, email
#what they purchase(sales) DB-> ID(num), date, name, product, quantity


#clients denotes class  #customer=table(database)
#sales=table(database)

import sys;
from tkinter import*
import sqlite3

class clients:
    
    #create customers database <-contains(ID, name, phone, email)
    def create_database():
        client_database = sqlite3.connect('client_data.db');
        c = client_database.cursor();
        
        #creating customers table
        c.execute('''CREATE TABLE customers (ID INT, name TEXT, phone TEXT, email TEXT)''')
        
        client_database.commit();
        client_database.close();
        print("NEW DATABASE CREATED\n");
    
    
    #creates the sales database <- contains id(called num) , date, name, product, quantity
    def create_sales_db():
        sales_db= sqlite3.connect('sales_data.db');
        c=sales_db.cursor();
        #creating sales table
        c.execute('''CREATE TABLE sales (num INT, date TEXT, name TEXT, product TEXT, quantity INT)''');
        sales_db.commit();
        sales_db.close();
        print("SALES DATABASE CREATED\n");
    
    #delete customer table
    def delete_database():
        client_database=sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''DROP TABLE customers''');
        client_database.commit();
        client_database.close();
    
    #delete sales table
    def delete_sales_db():
        sales_db=sqlite3.connect('sales_data.db');
        c=sales_db.cursor();
        c.execute('''DROP TABLE sales''');
        sales_db.commit();
        sales_db.close();
    
    #stores client info in database = adds client -> takes in name, phone, email
    def store_client_info(ID, name, phone, email):
        client_database = sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''INSERT INTO customers (ID ,name, phone, email) VALUES(?,?,?,?)''',(ID, name, phone, email));
        print("\nCLIENT INFO ENTERED:", name);
        client_database.commit();
        client_database.close();
    
    #retrieves all client information
    def retrieve_client_data():
        client_database = sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''SELECT ID, name, phone, email FROM customers''');
        customers=c.fetchall();
        print("\nRETRIEVING CLIENT DATA:");
        return customers;
    
    #retrieves all sales information
    def retrieve_all_sales():
        sales_db=sqlite3.connect('sales_data.db');
        c=sales_db.cursor();
        c.execute('''SELECT num, date, name, product, quantity FROM sales''');
        all_sales=c.fetchall();
        print("\nRETRIEVING ALL SALES DATA: ");
        return all_sales;
    
    
    #stores enteres information into one entry in the sales db
    def store_sales_info(num, date, name, product, quantity):
        sales_db=sqlite3.connect('sales_data.db');
        c=sales_db.cursor();
        c.execute('''INSERT INTO sales (num, date, name, product, quantity) VALUES(?,?,?,?,?)''',(num, date, name, product, quantity));
        print("\nSALES INFO ENTERED: ", num, name, product, quantity);
        sales_db.commit();
        sales_db.close();

    #retrieves all sales information in the sales db that contain tha matching product name
    def retrieve_sales_info(choice):
        print("\nRETRIEVING SALES INFO FOR:", choice);
        sales_db=sqlite3.connect('sales_data.db');
        c=sales_db.cursor();
        c.execute('''SELECT num, date, name, product, quantity FROM sales WHERE name=(?)''',[choice]);
        searchvar=c.fetchall();
        for row in searchvar:
            print(row);
                
                
                
    #retrieves the client information in the clients db that has the matching name
    def retrieve_one_client(n):
        print("\nRETRIEVING ONE CLIENT:", n);
        client_database=sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''SELECT ID, name, phone, email FROM customers WHERE name=(?) ''', [n]);
        searchvar=c.fetchall();
        for row in searchvar:
            print(row);


    #searches for all information in the clients and sales db that contain the matching name
    def search(searchname):
        print("\nSEARCHING FOR:", searchname);
        client_database=sqlite3.connect('client_data.db');
        sales_db=sqlite3.connect('sales_data.db');
        c=client_database.cursor();
        c.execute('''SELECT ID, name, phone, email FROM customers WHERE name=(?) ''', [searchname]);
        searchvar=c.fetchall();
        return searchvar;
    
    # searches for all information in sales db that contain the matching product name
    def searchbyprod(searchproduct):
        print("\nPRODUCT SEARCH:", searchproduct)
        sales_db=sqlite3.connect('sales_data.db');
        c=sales_db.cursor();
        c.execute('''SELECT num, date, name, product, quantity FROM sales WHERE product=(?)''', [searchproduct]);
        found_prod=c.fetchall();
        return found_prod;
    
    
    #deletes the client information that matches the inputted name (delete_name) from client database
    #information in sales database with matching name will not be deleted
    def delete_client(delete_name):
        client_database=sqlite3.connect('client_data.db');
        c=client_database.cursor();
        c.execute('''DELETE FROM customers WHERE name=(?) ''', [delete_name]);
        print("\nDELETED: ", delete_name); print("FROM DATABASE\n");
        client_database.commit();
        client_database.close();


