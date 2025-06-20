def add_contacts(file_name,name,number):
    with open(file_name, "a") as f:
        f.write(f"{name}: {number}\n")

def display_contacts(file_name):
    try:
        with open(file_name, "r") as f:
            contacts = f.readlines()
            if not contacts:
                print("No contacts found.")
                return
            for contact in contacts:
                print(contact.strip())
    except FileNotFoundError:
        print(f"The file {file_name} does not exist. Please add contacts first.")

def search_contact(file_name, search_name):
    try:
        with open(file_name, "r") as f:
            contacts = f.readlines()
            found = False
            for contact in contacts:
                name, number = contact.strip().split(": ")
                if name.lower() == search_name.lower():
                    print(f"Found: {name} -> {number}")
                    found = True
                    break
            if not found:
                print(f"No contact found with the name: {search_name}")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

