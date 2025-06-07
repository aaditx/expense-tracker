def add_expense():
    amount = input("Enter the amount: ")
    category = input("Enter the category like (Movie, Shopping etc...): ")
    note = input("Enter a note(optional): ")

    with open("expenses.txt", 'a') as f:
        f.write(f"{amount} | {category} | {note}\n")
        print("✅ Expense added!\n")


def view_expense():
    print("\n--- All Expenses ---")
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("No expenses recorded yet.")
    print()


def total_expenses():
    total = 0
    try:
        with open("expenses.txt", 'r') as f:
            for line in f:
                amount = line.split('|')[0].strip()
                total += float(amount)
        print(f"\n💰 Total Spent: ₹{total}\n")
    except FileNotFoundError:
        print("No expenses recorded yet.")
        return



while True:
    print("=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spent")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expense()
    elif choice == '3':
        total_expenses()
    elif choice == '4':
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")

