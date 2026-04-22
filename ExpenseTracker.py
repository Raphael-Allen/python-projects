import json
from datetime import date

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()
    
    def save_expenses(self):
        with open("expenses.json", "w") as f:
            json.dump(self.expenses, f)

    def load_expenses(self):
        try:
            with open("expenses.json", "r") as f:
                self.expenses = json.load(f)
        except FileNotFoundError:
            self.expenses = []

    def add_expense(self):
        while True:
            description = input("What is your new expense? ")
            amount = float(input("What is the amount? "))
            category = input("Add a category. ")
            today = date.today().strftime("%d/%m/%Y")
            expense = {"description": description, "amount": amount, "category": category, "date": today}
            self.expenses.append(expense)
            self.save_expenses()
            again = input("Press 1 to add another expense. Press 2 to go back")
            if again == "1":
                pass
            elif again == "2":
                return
            else:
                print("Error: Input not recognised")

    def view_expenses(self):
        if not self.expenses:
            print("You have no expenses yet.")
        else:
            for i, t in enumerate(self.expenses, start=1):
                print(f"{i}. {t['description']} - £{t['amount']:.2f} - {t['category']} - {t['date']}")
    
    def view_total(self):
        if not self.expenses:
            print("You have no expenses yet.")
        else:
            total = 0
            for expense in self.expenses:
                total += expense["amount"]
            print(f"Your total expenses are: £{total:.2f}")

    def delete_expense(self):
        self.view_expenses()
        remove = int(input("Select the task you want to remove by entering it's corresponding number")) - 1
        if 0 <= remove < len(self.expenses):
            self.expenses.pop(remove)
            self.save_expenses()
        else:
            print("Error: Entry doesn't exist")
    
    def filter_by_category(self):
        self.view_expenses()
        found = False
        check = input("Input a category: ")
        result = 0
        for i in self.expenses:
            if check.lower() == i["category"].lower():
                print(f"{i['description']} - £{i['amount']:.2f} - {i['category']} - {i['date']}")   
                found = True
                result += i["amount"]
        if found:   
            print(f"Total for {check}: £{result:.2f}")
        else:    
            print("Error: category doesn't exist")        
                
    
    def run(self):
        self.view_expenses()
        while True:
            selector = input("1. Add Expense 2. View Expenses 3. View Total 4. Delete Expense 5. Filter by Category 6. Quit ")
            if selector == "1":
                self.add_expense()
            elif selector == "2":
                self.view_expenses()
            elif selector == "3":
                self.view_total()
            elif selector == "4":
                self.delete_expense()
            elif selector == "5":
                self.filter_by_category()
            elif selector == "6":
                return
            else:
                print("Error: Input invalid")
    
              
expense = ExpenseTracker()
expense.run()

