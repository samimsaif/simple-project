Contact = {}

def ShowFunction():
    print(Contact.items())
    print("Name \t Contact")
    for x in Contact:
        print("{} \t {}".format(x, Contact.get(x)))
while True:
    choice = int(input("1. Add new contact \n"
                        "2. Search the contact \n"
                        "3. Display the contact \n"
                        "4. Edit the contact \n"
                        "5. Delete the contact \n"
                        "6. Exit \n"
                        "Please Write Number Between 1-6 : "))

    if choice == 1:
        name = input("Add your contact name: ")
        phone = input("Add your phone number: ")
        Contact[name] = phone
    elif choice == 2:
        contactName = input("Search the contact ")
        if contactName in Contact:
            print(contactName, " contact number is", Contact[contactName])
        else:
            print(" Not Found The Number")
    elif choice == 3:
        if not Contact:
            print("Contact book is Empty")
        else:
            ShowFunction()

    elif choice == 4:
        EditContact = input("Edit your Contact")
        if EditContact in Contact:
            phone = input("Change your Number")
            Contact[EditContact] = phone
            print(" Contact Updated Successfully")
            ShowFunction()
        else:
            print(" Name is not Found.")

    elif choice == 5:
        Del_Contact  = input(" Which contact do you want to delete..?")
        if Del_Contact in Contact:
            DeletedConfirm = input(" Do you want to delete the Contact  y/n")
            if DeletedConfirm == "y" or DeletedConfirm == "Y":
                Contact.pop(Del_Contact)
            ShowFunction()
        else:
            print(" The name is not found is contact list ")
    else:
        break
