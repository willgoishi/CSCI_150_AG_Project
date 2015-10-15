from incomeDB import incomeDB
from income import income

inDB = incomeDB()
inDB.createDB()

inMonth = str(raw_input("Input month: "))

ans = income(inMonth)
ans.month = inMonth

perform = str(raw_input("Input item? Y/N"))

if (perform == 'Y' || perform == 'y')
    ans.item = str(raw_input(("Item name: "))
    ans.amount = int(raw_input(("Amount sold: "))
    ans.price = int(raw_input(("Price of item: "))
    ans.income = price * amount

inDB.insertIntoDB(ans)
