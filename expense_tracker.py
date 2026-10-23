import json
import os
from datetime import date

# categories to choose from 
categories = {
    "1": "Food",
    "2": "Transportation",
    "3": "Shopping",
    "4": "Bills",
    "5": "Entertainment",
    "6": "Other"
}

# for uploading/creating the json to save the expenses
if os.path.exists("expenses.json"):
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
else:
    expenses = []

# A loop to save the expenses that were chosen 
while True:

    amount = float(input("\nHow much did you pay?"))

    print("\nChoose a category:")
    print("1. Food")
    print("2. Transportation")
    print("3. Shopping")
    print("4. Bills")
    print("5. Entertainment")
    print("6. Other")

    category_choice = input("Enter the number of the category: ")
    category = categories.get(category_choice, "Other")

    expense = {
        "amount": amount,
        "category": category,
        "date": str(date.today())
    }

    expenses.append(expense)

    print(f"\nYou spent AED{amount:.2f} on {category}.")

    another = input("\nDo you want to add another expense? (yes/no): ")

    if another.lower() != "yes":
        break

#dumping the data taken into the json file
with open("expenses.json", "w") as file:
    json.dump(expenses, file, indent=4)


total = sum(expense["amount"] for expense in expenses)

print(f"\nTotal spending: AED{total:.2f}")


category_totals = {}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category not in category_totals:
        category_totals[category] = 0

    category_totals[category] += amount


print("\nSpending by category:")

for category, total in category_totals.items():
    print(f"{category}: AED{total:.2f}")