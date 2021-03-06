#employee python file

#Employee - 
    #1:Input employee information and is able to store this information into database
    #2:Employee information can be extracted 
    #3:Employee's payroll and position standings are calculated and stored
    #4:Employees can be sorted based on precedence or ordered based on information

import sqlite3

def DatabaseConnection():
    return sqlite3.connect('EMPLOYEE\'S.db')

class EmployeesDatabase():
    def createTable(self):
        EmployeeDB = DatabaseConnection()   
        cursor = EmployeeDB.cursor()
        cursor.execute('''CREATE TABLE Employee\'s
                      (Name TEXT, Number TEXT, Email TEXT unique, Position TEXT, Salary TEXT)''')
        EmployeeDB.commit()
        EmployeeDB.close()

    def insertToTable(self, data):
        EmployeeDB = DatabaseConnection()
        cursor = EmployeeDB.cursor()
        cursor.execute('''
            INSERT INTO Employee\'s ( Name, Number, Email, Position, Salary) VALUES (?, ?, ?, ?, ?)''',
            (data.name, data.number, data.email, data.position, data.salary))
        EmployeeDB.commit()
        EmployeeDB.close()

    employeeInfo = []

    def retrieve_data(employeeInfo):
        EmployeeDB = DatabaseConnection()
        cursor = EmployeeDB.cursor();
        cursor.execute('''SELECT Name, Number, Email, Position, Salary FROM Employee\'s''');
        employeeInfo = cursor.fetchall();
        return employeeInfo;
