contacts = dict()

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
            contacts.update({newcontact_name:newcontact_number})
            print("Contact Updated Successfully")

        case 4:
            newcontact_name = input("Enter the name of the Contact: ")
            contacts.pop(newcontact_name)
            print("Contact Deleted Successfully")
            
        case _:
            print("Please enter a number between 1-7")






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

