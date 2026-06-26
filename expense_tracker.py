import csv
import os
from datetime import datetime

class ExpenseTracker:

    FILE_NAME = "expenses.csv"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Category", "Description", "Amount"])

    # Add Expense
    def add_expense(self):

        try:
            category = input("Enter Category: ")
            description = input("Enter Description: ")
            amount = float(input("Enter Amount: "))

            date = datetime.now().strftime("%Y-%m-%d")

            with open(self.FILE_NAME, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([date, category, description, amount])

            print("\nExpense Added Successfully!")

        except ValueError:
            print("Please Enter Valid Amount!")

    # View Expenses
    def view_expenses(self):

        with open(self.FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\nExpense Records")
            print("-" * 60)

            for row in reader:
                print(row)

    # Search Category
    def search_category(self):

        category_name = input("Enter Category: ")

        found = False

        with open(self.FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) > 1 and row[1].lower() == category_name.lower():
                    print(row)
                    found = True

        if not found:
            print("No Records Found!")

    # Monthly Summary
    def monthly_summary(self):

        total = 0

        with open(self.FILE_NAME, "r") as file:
            reader = csv.reader(file)

            next(reader)

            for row in reader:
                total += float(row[3])

        print(f"\nTotal Expense: ₹{total}")

    # Menu
    def menu(self):

        while True:

            print("\n===== PERSONAL EXPENSE TRACKER =====")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Search Category")
            print("4. Monthly Summary")
            print("5. Exit")

            choice = input("Enter Choice: ")

            if choice == "1":
                self.add_expense()

            elif choice == "2":
                self.view_expenses()

            elif choice == "3":
                self.search_category()

            elif choice == "4":
                self.monthly_summary()

            elif choice == "5":
                print("Thank You!")
                break

            else:
                print("Invalid Choice!")

tracker = ExpenseTracker()
tracker.menu()
