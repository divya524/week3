    # Add
import os
import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = set()

    def add_expense(self, amount, description, category):
        expense = {
            'date': datetime.datetime.now(),
            'amount': amount,
            'description': description,
            'category': category
        }
        self.expenses.append(expense)
        self.categories.add(category)

    def view_expenses(self):
        for expense in self.expenses:
            print(f"Date: {expense['date']} | Amount: {expense['amount']} | Description: {expense['description']} | Category: {expense['category']}")

    def view_summary(self):
        total_expenses = 0
        category_wise_expenses = {}
        for expense in self.expenses:
            total_expenses += expense['amount']
            if expense['category'] in category_wise_expenses:
                category_wise_expenses[expense['category']] += expense['amount']
            else:
                category_wise_expenses[expense['category']] = expense['amount']
        print(f"Total Expenses: {total_expenses}")
        for category, expense_amount in category_wise_expenses.items():
            print(f"{category}: {expense_amount}")

    def handle_user_input(self):
        while True:
            print("\n1. Add Expense")
            print("2. View Expenses")
            print("3. View Summary")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                category = input("Enter category: ")
                self.add_expense(amount, description, category)
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.view_summary()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

def main():
    tracker = ExpenseTracker()
    tracker.handle_user_input()

if __name__ == "__main__":
    main()