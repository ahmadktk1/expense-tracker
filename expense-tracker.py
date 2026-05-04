def add_expense(expenses):
    item = input("Enter expense name: ")
    amount = float(input("Enter amount in Rs: "))
    expenses.append((item, amount))
    print("Expense added!")
    return expenses

def show_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses yet!")
        return
    print("\n--- Your Expenses ---")
    total = 0
    for item, amount in expenses:
        print(item, ":", amount, "Rs")
        total += amount
    print("Total:", total, "Rs")

def save_expenses(expenses):
    file = open("expenses.txt", "w")
    for item, amount in expenses:
        file.write(item + "," + str(amount) + "\n")
    file.close()
    print("Expenses saved!")

def load_expenses():
    expenses = []
    try:
        file = open("expenses.txt", "r")
        for line in file:
            line = line.strip()
            parts = line.split(",")
            expenses.append((parts[0], float(parts[1])))
        file.close()
    except:
        print("No saved expenses found, starting fresh!")
    return expenses

def delete_item(expenses):
    item = input("Enter Expense item you want to delete : ")
    for i in range(len(expenses)):
        if item in expenses[i]:
            del expenses[i]
            save_expenses(expenses)
            return f"{item} deleted from expenses"
            # break
    return f"{item} not found in expenses"
    
    




expenses = load_expenses()

while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Delete Expense")
    print("4. Quit")
    choice = input("Choose: ")

    if choice == "1":
        expenses = add_expense(expenses)
    elif choice == "2":
        show_expenses(expenses)
    elif choice == "3":
        delete_item(expenses)
    elif choice == "4":
        save_expenses(expenses)
        break