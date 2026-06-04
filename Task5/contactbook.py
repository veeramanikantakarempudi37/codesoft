contacts = []

while True:
    print("\n----- CONTACT BOOK -----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        contacts.append(contact)
        print("Contact Added Successfully!")

    # View Contacts
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("-------------------")

    # Search Contact
    elif choice == "3":
        search = input("Enter Name or Phone Number: ")

        found = False

        for contact in contacts:
            if contact["name"] == search or contact["phone"] == search:
                print("\nContact Found")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("Address:", contact["address"])
                found = True

        if found == False:
            print("Contact Not Found!")

    # Update Contact
    elif choice == "4":
        name = input("Enter Name to Update: ")

        found = False

        for contact in contacts:
            if contact["name"] == name:
                contact["phone"] = input("New Phone: ")
                contact["email"] = input("New Email: ")
                contact["address"] = input("New Address: ")
                print("Contact Updated Successfully!")
                found = True

        if found == False:
            print("Contact Not Found!")

    # Delete Contact
    elif choice == "5":
        name = input("Enter Name to Delete: ")

        found = False

        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print("Contact Deleted Successfully!")
                found = True
                break

        if found == False:
            print("Contact Not Found!")

    # Exit
    elif choice == "6":
        print("Thank You for Using Contact Book!")
        break

    else:
        print("Invalid Choice! Please Try Again.")