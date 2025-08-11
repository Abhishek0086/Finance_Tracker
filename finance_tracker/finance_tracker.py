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
        self.Income = float(Income)
        self.Expense = float(Expense)
        self.Balance = Income - Expense
        self.Category = Category

    def to_dict(self):
        return {
            "UserName":self.UserName,
            "Income": self.Income,
            "Expense":self.Expense,
            "Balance":self.Income - self.Expense,
            "Category":self.Category
        }
    
    @staticmethod
    def save_to_file(data_list):
        with open('data.json','w') as f:
            json.dump(data_list,f,indent = 4)
            print("Data Uploaded!")
    @staticmethod
    def load_from_file():
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                print('DATA IN FILE:')
                for entry in data:
                    print(f"Name: {entry['UserName']}")
                    print(f"Income: ${entry['Income']}")
                    print(f"Expense: ${entry['Expense']}")
                    print(f"Balance: ${entry['Balance']}")
                    print(f"Category: {entry['Category']}")
                    print("-" * 30)
                return data
        except FileNotFoundError:
            print("No data file found!")
            return []
        except json.JSONDecodeError:
            print("File is empty or contains invalid JSON")
            return []
    @staticmethod
    def calculate_totals(data_list):
        total_income = sum(entry['Income'] for entry in data_list)
        total_expense = sum(entry['Expense'] for entry in data_list)
        net_balance = total_income - total_expense
        
        print(f"\n=== SUMMARY ===")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expense:.2f}")
        print(f"Net Balance: ${net_balance:.2f}")

    def search_username(data_list,val):
        for entry in data_list:
            if entry["UserName"].lower() == val:
                return True
        return False




# print('please choice the following options:')

# choice = int(input(print("Enter 1 to ADD details , Enter 2 to load the data or Enter 3 to quit" )))

# while choice:
#     case 1:
#         # some function call
#     case 2:
def main():

    data = []

    while True:
        print("\n" + "="*40)
        print("FINANCE TRACKER")
        print("="*40)
        print("1. Add new entry")
        print("2. Display all data")
        print("3. Show summary")
        print("4. user exists or not")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice :"))
        except ValueError:
            print("Invalid input, please enter a valid input!")

        match choice:
            case 1:
                while True:
                    try:
                    # each time user Enters data we pass it as argument to our function.
                        username = input("Enter your name")
                        income = float(input("Enter your income"))
                        expense = float(input("Enter your expense"))
                        category = input("Enter your category")
                        entry = {
                        "username": username,
                        "Income": income,
                        "Expense":expense,
                        "category":category,
                        }

                        d = Finance_Tracker(username,income,expense,category)
                        data.append(d.to_dict())

                        match = input("Do you wish to add more data, Enter y/n")
                        if match.lower() !="y":
                            Finance_Tracker.save_to_file(data)
                            print("Data saved successfully!")
                        break
                    except ValueError:
                        print("Invalid input, please enter numeric values for income and expense.")

            
            case 2:
                loader = Finance_Tracker.load_from_file()
                if loader:
                    print("Data loaded successfully!")
                else:
                    print("No data found or file is empty.")
            case 3:
                if not data:
                    loaded_data = Finance_Tracker.load_from_file()
                    if loaded_data:
                        Finance_Tracker.calculate_totals(loaded_data)
                    else:
                        print("No data available for summary.")
                else:
                    Finance_Tracker.calculate_totals(data)
            
            case 4:
                if data:  # Save data before exiting if there's unsaved data
                    save_choice = input("Do you want to save data before exiting? (y/n): ").lower()
                    if save_choice == 'y':
                        Finance_Tracker.save_to_file(data)
                print("Goodbye!")
                break
            case 5 :
                name = input('Enter the username for the data that you want to update:')
                if Finance_Tracker.search_username(data,name) == True :
                    print("User exists")
            
            case _:
                print("Invalid choice! Please try again.")

            
if __name__ == "__main__":
    main()





#if user want to update his data , first case we need to store his data in a database or else if username = username : allow editing 
# data["username"] = "username" then we can edit the rest of the info

#first - if user wants to update or delete his data
#converting data.json to sql and also updating the save method to sql
