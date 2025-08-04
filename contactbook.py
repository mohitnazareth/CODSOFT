class ContactBook:
    def __init__(self):
        self.contact = {}
    def add_contact(self, name, phone):
        if name in self.contact:
            print(f"Contact '{name}' already exists. Updating phone number. ")
        self.contacts[name] = phone               
        print(f"Contact '{name}' added/updated successsfully.")
    def view_contacts(self):
        if not self.contacts:
            print("No contact found")
            return
        print("contact list: ")
        for name, phone in self.contacts.items():
            print(f"{name}: {phone}")
    def search_contact(self, name):
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]}")
        else :
            print(f"Contact '{name}' not found.")
def main():
    contact_book = ContactBook

    while True:
        print("\nContact book menu:")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contacts")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            contact_book.add_contact(name, phone)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice =='3':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice =='4':
            print("Exiting the contact book. ")
            break    
        else :
            print("invalid choice. Please try again.")
if __name__ == "__main__":
    main()            