contacts = dict()
tasks = dict()
accounts = dict()

def Contacts(contacts):
    # contacts = {name : phone_number}
    print("Welcome to Contacts\n" 
    "1. Add Contacts\n"
    "2. Search Contacts\n"
    "3. Update Contacts\n"
    "4. Delete Contacts\n")
    contacts_menu = int(input("Please enter an integer between 1-4: "))

    match contacts_menu:
        case 1:
            newcontact_name = input("Enter the name of the Contact: ")
            newcontact_number = input("Enter the phone number of the Contact: ")
            contacts.update({newcontact_name:newcontact_number})
            print("Contact Added Successfully")
            
        case 2:
            newcontact_name = input("Enter the name of the Contact: ")
            if newcontact_name in contacts:
                print(newcontact_name, ":", contacts[newcontact_name])
            else:
                print("Contact not found")

        case 3:
            newcontact_name = input("Enter the name of the Contact: ")
            newcontact_number = input("Enter the new phone number of the Contact: ")
            if newcontact_name in contacts:
                contacts.update({newcontact_name:newcontact_number})
                print("Contact Updated Successfully")
            else:
                print("Contact not found")

        case 4:
            newcontact_name = input("Enter the name of the Contact: ")
            if newcontact_name in contacts:
                contacts.pop(newcontact_name)
                print("Contact Deleted Successfully")
            else:
                print("Contact not found")
            
        case _:
            print("Please enter a number between 1-7")

def Tasks(tasks):
    # tasks = {task_name : status}
    print("Welcome to Tasks\n" 
    "1. Add Task\n"
    "2. Mark Complete\n"
    "3. Delete Task\n")
    tasks_menu = int(input("Please enter an integer between 1-3: "))

    match tasks_menu:
        case 1:
            newtask_name = input("Enter the name of the new task (set as incomplete by default): ")            
            tasks.update({newtask_name:"Incomplete"})
            print("Task Added Successfully")
            
        case 2:
            task_name = input("Enter the name of the task you want to set as complete: ")
            if task_name in tasks:
                tasks.update({task_name:"Complete"})
                print("Task set as Complete Successfully")

            else:
                print("Task not found")

        case 3:
            task_name = input("Enter the name of the Contact: ")
            if task_name in tasks:
                tasks.pop(task_name)
                print("Task Deleted Successfully")
            else:
                print("Task not found")

        case _:
            print("Please enter a number between 1-3")

class Account():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def Deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def Withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient Funds"
    def ViewBalance(self):
        return self.balance

def BankMenu(accounts):
    print("Welcome to Bank\n" 
    "1. Add an Account\n"
    "2. Deposit Money\n"
    "3. Withdraw Money\n"
    "4. View Balance\n")
    bank_menu = int(input("Please enter an integer between 1-4: "))

    match bank_menu:
        case 1:
            accountholder_name = input("Enter the name of the account holder: ")
            accountholder_balance = int(input("Enter the balance of the account: "))
            accounts.update({accountholder_name: Account(accountholder_name, accountholder_balance)})
            print("Account Added Successfully")
            
        case 2:
            accountholder_name = input("Enter the name of the Account: ")
            amount = int(input("Enter the amount you want to deposit: "))
            account = accounts.get(accountholder_name)
            new_balance = account.Deposit(amount)
            print("New Balance: ", new_balance)

        case 3:
            accountholder_name = input("Enter the name of the Account: ")
            amount = int(input("Enter the amount you want to Withdraw: "))
            account = accounts.get(accountholder_name)
            new_balance = account.Withdraw(amount)
            print("New Balance: ", new_balance)

        case 4:
            accountholder_name = input("Enter the name of the Account: ")
            account = accounts.get(accountholder_name)
            balance = account.ViewBalance()
            print("Balance : ", balance)
            
        case _:
            print("Please enter a number between 1-4")

def Analytics(): 
    text = input("Enter the text (please avoid any extra spaces): ")
    words = text.split()
    count = len(words)
    print("Word Count: ", count)

def GridExplorer():
    Grid = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

    player = [1, 1]

    while True:

        temp = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]

        row, col = player
        temp[row][col] = "P"

        for r in temp:
            print(r)

        direction = input("Move (WASD), E for Exit: ").lower()

        if direction == "e":
            break

        new_row, new_col = player

        if direction == "w":
            new_row -= 1
        elif direction == "s":
            new_row += 1
        elif direction == "a":
            new_col -= 1
        elif direction == "d":
            new_col += 1

        if 0 <= new_row <= 2 and 0 <= new_col <= 2:
            player[0] = new_row
            player[1] = new_col


    

while True:
    print("Welcome to Life Manager System\n"
      "1. Contacts\n"
      "2. Tasks\n"
      "3. Bank Account\n"
      "4. Analytics\n"
      "5. Grid Explorer\n"
      "6. Save / Load\n"
      "7. Exit")
    menu_input = int(input("Please enter an integer between 1-7: "))

    match menu_input:
        case 1:
            Contacts(contacts)
        case 2:
            Tasks(tasks)
        case 3:
            BankMenu(accounts)
        case 4:
            Analytics()
        case 5:
            GridExplorer()
        case 6:
            #call function for Save/Load
            pass
        case 7:
            break
        case _:
            print("Please enter a number between 1-7")

