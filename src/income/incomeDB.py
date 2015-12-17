import sqlite3

def ConnectDatabase():
        return sqlite3.connect('IncomeDatabase.db') 
    
class incomeDB():
        database = ConnectDatabase()  
        item = database.cursor()

        def createDB(self):
                self.item.execute('''CREATE TABLE IncomeDatabase (Month INTEGER, Year INTEGER, Amount INTEGER, Income INTEGER)''')
                database.commit()
                database.close()

        def insertIntoDB(self, data):
                self.database = ConnectDatabase()
                self.item = self.database.cursor()
                self.item.execute('''INSERT INTO IncomeDatabase ( Month, Year, Amount, Income) VALUES (?, ?, ?, ?)''',
                             (data.month, data.year, data.amount, data.income))
                self.database.commit()
                self.database.close()

        def getInfo(self):
                self.database = ConnectDatabase()
                self.item = self.database.cursor()
                info = self.item.execute('SELECT * FROM IncomeDatabase ORDER BY Year, Month')
                return info
