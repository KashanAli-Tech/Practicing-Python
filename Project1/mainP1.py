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
            #call function for Contacts
            pass
        case 2:
            #call function for Tasks
            pass
        case 3:
            #call function for Bank Account
            pass
        case 4:
            #call function for Analytics
            pass
        case 5:
            #call function for Grid Explorer
            pass
        case 6:
            #call function for Save/Load
            pass
        case 7:
            break
        case _:
            print("Please enter a number between 1-7")
