from db import add_expense, get_expenses

def print_menu():
    print("\n💸 Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            category = input("Enter category (food, bills, etc): ")
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("⚠️ Invalid amount. Try again.")
                continue
            description = input("Optional description: ")
            add_expense(category, amount, description)
            print("✅ Expense added!")
        elif choice == '2':
            expenses = get_expenses()
            if expenses:
                print("\nYour Expenses:")
                print("ID | Category | Amount | Description")
                print("-" * 40)
                for exp in expenses:
                    print(f"{exp[0]} | {exp[1]} | ₹{exp[2]} | {exp[3]}")
            else:
                print("No expenses found.")
        elif choice == '3':
            print("👋 Exiting. Stay thrifty!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
