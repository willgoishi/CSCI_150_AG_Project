import sqlite3

def ConnectDatabase():
        return sqlite3.connect('itemDB.db'); 
    
class incomeDB():
    def createDB(self):
        database = ConnectDatabase()  
        item = database.cursor()
        item.execute('''CREATE TABLE IncomeDatabase
                      (Month TEXT, Item TEXT, Amount INTEGER, Price INTEGER, Income INTEGER)''')
        database.commit()
        database.close()

    def insertIntoDB(self, data):
        database = DatabaseConnection()
        item = database.cursor()
        item.execute('''
            INSERT INTO IncomeDatabase ( Month, Item, Amount, Price, Income) VALUES (?, ?, ?, ?, ?)''',
            (data.month, data.item, data.amount, data.price, data.income))
        database.commit()
        database.close()

    def getInfo(self):
        database = ConnectDatabase()
        item = database.cursor()
        info = item.execute('SELECT * FROM IncomeDatabase ORDER BY Month')
        return info

    

    
