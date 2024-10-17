import json
from datetime import datetime
import matplotlib.pyplot as plt

# File to save expenses
FILE_NAME = "expenses.json"

# Load expenses from file
def load_expenses():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
    date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ")
    
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    
    expense = {
        'amount': amount,
        'category': category,
        'date': date
    }
    
    expenses.append(expense)
    print("Expense added!")
    save_expenses(expenses)

# View summaries
def view_summary(expenses):
    print("1. Total spending by category")
    print("2. Total overall spending")
    print("3. Spending by time (daily/weekly/monthly)")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        category = input("Enter category: ")
        total = sum(exp['amount'] for exp in expenses if exp['category'].lower() == category.lower())
        print(f"Total spent on {category}: ${total:.2f}")
    
    elif choice == '2':
        total = sum(exp['amount'] for exp in expenses)
        print(f"Total overall spending: ${total:.2f}")
    
    elif choice == '3':
        view_spending_over_time(expenses)
    else:
        print("Invalid option")

# View spending over time (daily, weekly, or monthly)
def view_spending_over_time(expenses):
    time_choice = input("View spending by (daily/weekly/monthly): ").lower()
    
    if time_choice == "daily":
        view_spending_by_day(expenses)
    elif time_choice == "weekly":
        # Logic to sum expenses by week can go here
        pass
    elif time_choice == "monthly":
        # Logic to sum expenses by month can go here
        pass
    else:
        print("Invalid option.")

# View spending by day
def view_spending_by_day(expenses):
    daily_summary = {}
    for exp in expenses:
        date = exp['date']
        if date not in daily_summary:
            daily_summary[date] = 0
        daily_summary[date] += exp['amount']
    
    for date, total in daily_summary.items():
        print(f"{date}: ${total:.2f}")

# Delete or edit an expense (Bonus)
def modify_expense(expenses):
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['date']} - {exp['category']}: ${exp['amount']:.2f}")
    
    choice = int(input("Enter the number of the expense to delete/edit: ")) - 1
    if 0 <= choice < len(expenses):
        action = input("Enter 'd' to delete or 'e' to edit: ").lower()
        if action == 'd':
            expenses.pop(choice)
            print("Expense deleted!")
        elif action == 'e':
            expenses[choice]['amount'] = float(input("Enter the new amount: "))
            expenses[choice]['category'] = input("Enter the new category: ")
            expenses[choice]['date'] = input("Enter the new date (YYYY-MM-DD): ")
            print("Expense updated!")
        save_expenses(expenses)
    else:
        print("Invalid selection")

# Graphical summary of expenses (Bonus)
def plot_expenses(expenses):
    categories = {}
    for exp in expenses:
        category = exp['category']
        categories[category] = categories.get(category, 0) + exp['amount']
    
    plt.bar(categories.keys(), categories.values())
    plt.title('Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Spending')
    plt.show()

# Main menu
def menu():
    expenses = load_expenses()
    
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add an expense")
        print("2. View summary")
        print("3. Delete/Edit an expense")
        print("4. View graphical summary")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            modify_expense(expenses)
        elif choice == '4':
            plot_expenses(expenses)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
