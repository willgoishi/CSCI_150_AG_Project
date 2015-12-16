import sqlite3

def DatabaseConnection():
    return sqlite3.connect('EMPLOYEES.db')

class EmployeesDatabase():
    def createTable(self):
        EmployeeDB = DatabaseConnection()   # the database is assign to the variable InventoryDB
        cursor = EmployeeDB.cursor()
        cursor.execute('''CREATE TABLE Employees
                      (Name TEXT, Number TEXT, Email TEXT unique, Position TEXT, Salary TEXT)''')
        EmployeeDB.commit()
        EmployeeDB.close()

    def insertToTable(self, data):
        EmployeeDB = DatabaseConnection()
        cursor = EmployeeDB.cursor()
        cursor.execute('''
            INSERT INTO Employees ( Name, Number, Email, Position, Salary) VALUES (?, ?, ?, ?, ?)''',
            (data.name, data.number, data.email, data.position, data.salary))
        EmployeeDB.commit()
        EmployeeDB.close()


    def retrieve_data(self):
        employeeInfo = []
        EmployeeDB = DatabaseConnection();
        cursor = EmployeeDB.cursor();
        cursor.execute('''SELECT Name, Number, Email, Position, Salary FROM Employees''');
        employeeInfo = cursor.fetchall();
        return employeeInfo;

    def delete_table(self):
        EmployeeDB = DatabaseConnection();
        cursor = EmployeeDB.cursor();
        cursor.execute('''DROP TABLE Employees''')
        EmployeeDB.commit()
        EmployeeDB.close()
