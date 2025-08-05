# we want to build a cli based finance tracker
#That allows users to track their expenses and income

#Enter income and expenses

# Categorize and track them

# Save data to a file

# Load data back from the file

# Calculate total income, total expense, and balance
import json

class Finance_Tracker:
    def __init__(self,UserName,Income,Expense,Category):
        self.UserName = UserName
        self.Income = Income
        self.Expense = Expense
        self.Balance = Income - Expense
        self.Category = Category

    def save_to_file(self):
        data = {
            "UserName":self.UserName,
            "Income": self.Income,
            "Expense":self.Expense,
            "Balance":self.Income - self.Expense,
            "Category":self.Category
        }
        with open('data.json','w') as f:
            json.dump(data,f,indent = 4)
            print("Data Uploaded!")