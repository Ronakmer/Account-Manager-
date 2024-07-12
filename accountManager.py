import json
from datetime import datetime

filePath = 'transactions.json'


def readTransactions():
    try:
        with open(filePath, 'r') as file:
            transactionData = json.load(file)
    except Exception as e:
        transactionData = []
    return transactionData


def writeTransactions(transactionData):
    with open(filePath, 'w') as file:
        json.dump(transactionData, file)


def addTransaction(description, amount, category, TransactionDate = None):
    
    if TransactionDate is None:
        TransactionDate = datetime.now().strftime('%Y-%m-%d')

    
    transactionData = {
        "date" : TransactionDate,
        "amount" : amount,
        "category" : category,
        "description" : description
    }

    readTransactionsObj = readTransactions()
    readTransactionsObj.append(transactionData)
    writeTransactions(readTransactionsObj)
    
    
def summary():
    readTransactionsObj = readTransactions()
    
    totalIncome = 0
    totalExpenses = 0
    
    for TransactionAmount in readTransactionsObj:
        amount = float(TransactionAmount['amount'])
        if amount > 0:
            totalIncome += amount
        else:
            totalExpenses += amount
            
        balance = totalIncome - totalExpenses
                
    print()
    print("Summary Report:")
    print(f"Total Income: {totalIncome}")
    print(f"Total Expenses: {totalExpenses}")
    print(f"Current Balance: {balance}")
    print("***************************")


def summaryDate(summaryDates = None):
    
    if summaryDates is None:
        summaryDates = datetime.now().strftime('%Y-%m-%d')
        
    transactions = readTransactions()
    for transaction in transactions:
        if transaction["date"] == summaryDates:
            print()
            print("Date Summary:")
            print(f"Transaction Date: {transaction['date']}")
            print(f"Transaction Amount: {transaction['amount']}")
            print(f"Transaction Category: {transaction['category']}")
            print(f"Transaction Description: {transaction['description']}")
            print("***************************")

        
def menu():
    while True:
        print("Personal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Summary Report")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            TransactionDate = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            TransactionDate = TransactionDate if TransactionDate else None
            addTransaction(description, amount, category, TransactionDate)
        elif choice == '2':
            summary()
            while True:
                print("Summary Tracker")
                print("1. Enter Date")
                print("2. Exit")
                
                choice = input("Enter your choice: ")
                
                if choice == '1':
                    summaryDates = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
                    summaryDates = summaryDates if summaryDates else None
                    summaryDate(summaryDates)
                    
                elif choice == '2':
                    print("Goodbye summary !")
                    break
                else:
                    print("Invalid choice. Please try again.")
                
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    menu()

