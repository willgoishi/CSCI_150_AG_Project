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
    
    def __init__(self, day, month, year): #Initiates Time factors for Records Class
        self.day = None;
        self.month = None;
        self.year = None;

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
        
     def compare_sales_records():#Allows comparison between different years of sales
        
        def calculate_cost(cost_list): #calculates cost and acts as a helper function to calculate total costs of a given year 
            total_cost = 0;                             #sets total cost to zero
            for x in cost_list:                         #iterates through array to obtain all the costs
                total_cost = total_cost + x;                #adds costs up and stores them into total_cost
            return total_cost;                          #returns the total_cost <used later for comparison>
        
        database = sqlite3.connect('records_information_sales.db');    #Opens Database <sales_information>

        controller = database.cursor();
        id_num = []         #Array to store id numbers
        year_sales = [];    #Array to store years that items were sold
        sale_costs = [];    #Array to store the cost of sales <used for processing sales totals>
        
        database_sales = database.execute('SELECT id, cost, year FROM sale ');#selects the three info_types <id,cost,year> from database sale <retrieves the data>
        for row in database_sales:        #iterates through selected info from database by row  
            id_num.append(row[0]);          #Stores first line of info <id numbers> and stores them in the id_num array
            sale_costs.append(row[1]);      #Stores second line of info <costs> and stores them into the sale_costs array
            year_sales.append(row[2]);      #Stores third line of info <years> and stores them into the year_sales array
            
        n = 0;                   #n is declared to zero value and used for place holder for first iteration
        m = n+1;                 #m equals n + 1 and is used for the second value iteration 
        record = [];             #Records array called
        
        while n<len(id_num):                                 #While n is less than the length of id_num array, will...
            
            cost = sale_costs[n];                            #...initialize cost to the value of sale_costs[n]...from array above
            while n < (len(id_num)) and m < (len(id_num)):   #While length of n and m are both less than id_num length can continue through and then increment m
                if year_sales[n] == year_sales[m]:               #Checks if a year at <n> is equal to a year at <m> which is the next year in the list of year_sales
                    cost = cost + sale_costs[m];                   #If so then will add that m value sale_costs to the total which is called <cost> 
                else:                                            #else will do nothing
                    print();
            
                m += 1;                                          #increments <m> so that it can loop again in the while statement and traverse through the list checking for equal years
                
            if not (year_sales[n] in record):                           ##This checks whether we printed a year already by storing years in a list then checking if they are in the list or not
                print("Year:",year_sales[n],"Total_Income: $",cost);          #prints the year and the total sum of the income
                record.append(year_sales[n]);                                 #appends the year to the array <record>
                #print(record);

            n += 1;                                              #increments <n> then goes back to the main loop to then traverse the list through <m> value
            m = n + 1;                                           #re-initializes <m> value back to n + 1 otherwise it'll stay at <4> which causes a logical error
            
        print("Cost for all years in Database:","$",calculate_cost (sale_costs));    #Prints the total of the costs in the array
        database.commit(); #commits all actions related to the database

        database.close();    #closes database
        
    def create_database_payroll():                                                  #creates database payroll that will store payroll for employees
        database = sqlite3.connect('payroll.db');
        c = database.cursor();
        c.execute('''CREATE TABLE payroll (name TEXT, year TEXT, salary INTEGER) ''');
        database.commit();
        database.close();

    def store_employee_with_salary(name_employee, year_paid, salary_amount):        #stores a single set of data relating to one individual's salary for a year
        database = sqlite3.connect('payroll.db');
        cursor = database.cursor();
        cursor.execute('''INSERT INTO payroll(name, year, salary) VALUES (?,?,?) ''',(name_employee, year_paid, salary_amount));
        database.commit();
        database.close();

    def delete_payroll_database():
        database = sqlite3.connect('payroll.db');
        c = database.cursor();
        c.execute('''DROP TABLE payroll ''');
        database.commit();
        database.close();
        
    def print_payroll_from_designated_year(year):                                   #Prints the salary for a year based on what year user inputs 
        database = sqlite3.connect('payroll.db');
        controller = database.cursor();

        year_salary_paid = []; #array to store the years at which salaries were paid
        salary = [];           #array to store the salary values that were actually paid
        payroll_year = [];     #array that will be used to store years so that it will revoke repetitive printing of yearly payrolls
        
        database_payroll = database.execute('SELECT year, salary FROM payroll');  #executes a database command that will retrieve the data by row from database
        for row in database_payroll:            #this segment takes the information from the database and stores them seperately into individual arrays
            year_salary_paid.append(row[0]);
            salary.append(row[1]);
            
        #section that sorts years and adds similar salaries for a year and prints out the salaries for the desired year    
        a = 0;   #first tracer for traversal through array
        b = a+1; #second tracer for traversal through array
        
        while a < len(year_salary_paid):
            salary_prime = salary[a]; #sets the value of salary_prime
            while a < len(year_salary_paid) and b < len(year_salary_paid):     #as long as the length of a and b are less than size of salary year_salary array...
                if(year_salary_paid[a] == year_salary_paid[b]):                #then can allow the following to take place, meaning it checks if array is empty or not
                    salary_prime = salary_prime + salary[b];     #if the years are matching for different segments of the array, then it adds the salaries towards a total sum
                    b += 1;                                 # increments b to allow traversal through the array
                else:
                    b += 1;                                 # increments b to allow traversal through the array
                
            if not (year_salary_paid[a] in payroll_year): #condition set to check if a year has been seen and printed already
                if year == year_salary_paid[a]:
                    print("Year:", year_salary_paid[a], "Payroll Total For Year:", salary_prime); #prints the year and the total payroll for that year
                elif year != year_salary_paid[a]:
                    pass;
                else:    #checks and print not recorded if the data doesnt exist in memory
                    print("Error: Date Not Recorded");
                payroll_year.append(year_salary_paid[a]); #appends the year into the payroll_year so that future printing of the same data does not occur

            a += 1; #increments the first position to the next so another traversal can take place 
            b = a + 1;#resets the value of <b>
        database.commit();
        database.close();
