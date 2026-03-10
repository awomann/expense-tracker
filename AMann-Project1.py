# ————— STEP 1: ADDING AN EXPENSE —————

# Line 4 is where all expenses will be stored.
import csv
expenses = []
budget = 0

# Defining the function which can be used each time a new expense is added.
def add_expense():
    date = input("Enter the expense date in YYYY-MM-DD format: ")
    category = input("Enter the category. Ex: Food or Travel: ")
    amount = float(input("Enter the expense amount: "))
    description = input("Enter the expense purpose: ")
    
    # Creating the dictionary which pulls from the variables in the function.
    expense = {
        "date" : date,
        "category" : category,
        "amount" : amount,
        "description" : description,
        }
    
    expenses.append(expense)
    print("Expense successfully added.")

""" STEP 1 COMPLETE: ADDING AN EXPENSE 
We defined a global variable which any function can access. We also defined the first function for adding expenses; this establishes a set of instructions to follow any time a new expense is added. Inside the function, we created a dictionary which pulls from the variables in the function. The dictionary is a set of with labels that works with the function variables. """


# ————— STEP 2: VIEWING AN EXPENSE —————

# Defining a function to view expenses.
def view_expenses():
    if expenses:
        for expense in expenses:
            print("Date:", expense["date"])
            print("Category:", expense["category"])
            print("Amount:", expense["amount"])
            print("Description:", expense["description"])
    else:
        print("Please enter an expense first.")

""" STEP 2 COMPLETE: VIEWING AN EXPENSE 
We defined a new fucntion to view expenses. We also added a decision here to first check to see if there are items in the list of expenses. If so, follow the function instructions. If not, print the message under else. """


# ————— STEP 3: SET AND TRACK A BUDGET —————

# Define function to have the user set a budget.
def set_budget():
    global budget
    budget = float(input("Enter your budget."))

# A function for totaling current expenses and showing the remainder of the budget.
def track_budget():
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    if total >= budget:
        print("You've exceeded your budget.")
    else:
        print("You have this much left in your budget:", (budget - total))

""" STEP 3 COMPLETE: SET AND TRACK A BUDGET
Here, we set 2 functions. The first one allows the user to set a budget. The second one shows the user how they're tracking against that budget and also the remainder of the budget if that applies. Steps 1 through 3 define how the program works before we allow it to access a file."""


# ————— STEP 4: LOADING FROM A CSV —————

# Function for grabbing expenses from the expenses list above. Python will consolidate them all and save them to 1 CSV called expenses.csv.
def save_expenses():
    with open("expenses.csv", "w") as file:
        writer = csv.writer(file)
        for expense in expenses:
            writer.writerow([expense["date"], expense["category"], expense["amount"], expense["description"]])

# Function for loading the expenses back into the CSV file.
def load_expenses():
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            expense = {
                "date" : row[0],
                "category" : row[1],
                "amount" : float(row[2]),
                "description" : row[3],
            }
            expenses.append(expense)

""" STEP 4 COMPLETE: LOADING FROM A CSV
Here, we set 2 functions. The first grabs expenses from the stored expenses in the expenses list above. Python then writes them to a new CSV. In the end, there would be a new CSV that Python makes that's in that folder. The second function rebuilds the expenses from that same CSV back to the expenses list as it's defined above. """



# ————— STEP 5: INTERACTIVE MENU —————

# Function for creating the interactive menu with a loop inside.
def main_menu():
        
    while True:
        print("1. Add expense")
        print("2. View expense")
        print("3. Set budget")
        print("4. Track budget")
        print("5. Save expenses")
        print("6. Exit")

        selection = input("Enter your selection: ")
       
        if selection == "1":
            add_expense()
        elif selection == "2":
            view_expenses()
        elif selection == "3":
            set_budget()
        elif selection == "4":
            track_budget()
        elif selection == "5":
            save_expenses()
        else:
            print("Done")
            break

# Trying to fetch some expenses from a CSV first before calling the menu function.
try:
    load_expenses()
except FileNotFoundError:
    print("No saved expenses found. Select option 1 to add your first expense!")

main_menu()

""" STEP 5 COMPLETE: INTERACTIVE MENU
Here, we set the function for the interactive menu. Before calling the function, we attempt to load any previously saved expenses from the CSV file. In the menu, the user can select a number of options to execute certain actions. We've added an additional option to set the budget so there's a budget to track. """