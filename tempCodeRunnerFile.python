expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    note = input("Enter note: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }

    expenses.append(expense)

def view_expenses():
    for i in expenses:
        print(i["amount"], "|", i["category"], "|", i["note"])

def total_spent():
    total = sum(i["amount"] for i in expenses)
    print("Total spent:", total)

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spent")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spent()
    elif choice == "4":
        break