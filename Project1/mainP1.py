import json

datafile_read = open("Project1/Data.json", "r")
data = json.load(datafile_read)

contacts = data["contacts"]
tasks = data["tasks"]
accounts = data["bank"]

datafile_read.close()


def WriteFile():
    datafile_write = open("Project1/Data.json", "w")

    maindata = {
        "contacts": contacts,
        "tasks": tasks,
        "bank": accounts
    }

    json.dump(maindata, datafile_write)

    datafile_write.close()


def Contacts(contacts):

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
            contacts[newcontact_name] = newcontact_number

        case 2:
            newcontact_name = input("Enter the name of the Contact: ")
            if newcontact_name in contacts:
                print(newcontact_name, ":", contacts[newcontact_name])

        case 3:
            newcontact_name = input("Enter the name of the Contact: ")
            newcontact_number = input("Enter the new phone number of the Contact: ")
            if newcontact_name in contacts:
                contacts[newcontact_name] = newcontact_number

        case 4:
            newcontact_name = input("Enter the name of the Contact: ")
            if newcontact_name in contacts:
                contacts.pop(newcontact_name)

        case _:
            pass


def Tasks(tasks):

    print("Welcome to Tasks\n"
          "1. Add Task\n"
          "2. Mark Complete\n"
          "3. Delete Task\n")

    tasks_menu = int(input("Please enter an integer between 1-3: "))

    match tasks_menu:

        case 1:
            newtask_name = input("Enter the name of the new task: ")
            tasks[newtask_name] = "Incomplete"

        case 2:
            task_name = input("Enter the name of the task: ")
            if task_name in tasks:
                tasks[task_name] = "Complete"

        case 3:
            task_name = input("Enter the name of the task: ")
            if task_name in tasks:
                tasks.pop(task_name)

        case _:
            pass


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

            if accountholder_name in accounts:
                print("Account already exists")
            else:
                accounts[accountholder_name] = accountholder_balance
                print("Account Added Successfully")

        case 2:
            accountholder_name = input("Enter the name of the Account: ")

            if accountholder_name in accounts:
                amount = int(input("Enter the amount you want to deposit: "))
                accounts[accountholder_name] += amount
                print("New Balance:", accounts[accountholder_name])
            else:
                print("Account not found")

        case 3:
            accountholder_name = input("Enter the name of the Account: ")

            if accountholder_name in accounts:
                amount = int(input("Enter the amount you want to Withdraw: "))

                if accounts[accountholder_name] >= amount:
                    accounts[accountholder_name] -= amount
                    print("New Balance:", accounts[accountholder_name])
                else:
                    print("Insufficient Funds")
            else:
                print("Account not found")

        case 4:
            accountholder_name = input("Enter the name of the Account: ")

            if accountholder_name in accounts:
                print("Balance:", accounts[accountholder_name])
            else:
                print("Account not found")

        case _:
            print("Please enter a number between 1-4")

        


def Analytics():
    text = input("Enter the text: ")
    print("Word Count:", len(text.split()))


def GridExplorer():

    player = [1, 1]

    while True:

        temp = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]

        r, c = player
        temp[r][c] = "P"

        for row in temp:
            print(row)

        move = input("Move (WASD), E to exit: ").lower()

        if move == "e":
            break

        row, col = player

        if move == "w":
            row -= 1
        elif move == "s":
            row += 1
        elif move == "a":
            col -= 1
        elif move == "d":
            col += 1

        if 0 <= row <= 2 and 0 <= col <= 2:
            player = [row, col]


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
            WriteFile()

        case 7:
            WriteFile()
            break

        case _:
            print("Please enter an integer between 1-7: ")