class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        new_contact = Contact(name, phone_number, email, address)
        self.contacts.append(new_contact)
        print(f"Contact added: {new_contact}")

    def view_contact_list(self):
        print("Contact List:")
        for contact in self.contacts:
            print(contact)

    def search_contact(self, search_term):
        search_results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term.lower() in contact.phone_number]
        if search_results:
            print("Search Results:")
            for contact in search_results:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self, name, new_phone_number, new_email, new_address):
        contact_to_update = next((contact for contact in self.contacts if contact.name == name), None)
        if contact_to_update:
            contact_to_update.phone_number = new_phone_number
            contact_to_update.email = new_email
            contact_to_update.address = new_address
            print(f"Contact updated: {contact_to_update}")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        contact_to_delete = next((contact for contact in self.contacts if contact.name == name), None)
        if contact_to_delete:
            self.contacts.remove(contact_to_delete)
            print(f"Contact deleted: {name}")
        else:
            print("Contact not found.")

def main():
    contact_manager = ContactManager()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone_number, email, address)
        elif choice == 2:
            contact_manager.view_contact_list()
        elif choice == 3:
            search_term = input("Enter search term: ")
            contact_manager.search_contact(search_term)
        elif choice == 4:
            name = input("Enter name of contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_manager.update_contact(name, new_phone_number, new_email, new_address)
        elif choice == 5:
            name = input("Enter name of contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()