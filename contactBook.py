# Initialize an empty dictionary to store contacts
contacts = {}

# Function to add a contact
def add_contact(name, phone, email):
    if name in contacts:
        print(f"Contact with name {name} already exists.")
    else:
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} added successfully.")

# Function to search for a contact
def search_contact(name):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"Contact with name {name} not found.")

# Function to update a contact
def update_contact(name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact with name {name} not found.")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact with name {name} not found.")

# Function to display all contacts
def display_contacts():
    if contacts:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("No contacts found.")

# Main function to display the menu and handle user input
def contact_book():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == '3':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (press enter to skip): ")
            email = input("Enter new email (press enter to skip): ")
            update_contact(name, phone if phone else None, email if email else None)
        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the contact book program
contact_book()
