import json
import os

class ContactManager:
    def __init__(self, file_path="contact.json"):
        self.file_path = file_path
        self.contact_list = []
        self._load_contacts_from_file()

    def _load_contacts_from_file(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({"contacts": []}, f, indent=4)

        with open(self.file_path, 'r') as f:
            try:
                file_data = json.load(f)
                self.contact_list = file_data.get("contacts", [])
            except json.JSONDecodeError:
                self.contact_list = []

    def _save_to_file(self):
        with open(self.file_path, 'w') as f:
            json.dump({"contacts": self.contact_list}, f, indent=4)

    #  Add a contact
    def add(self, id, name, phone_number):
        new_contact = {"id": id, "name": name, "phone_number": phone_number}
        self.contact_list.append(new_contact)
        self._save_to_file()
        print(f" Contact '{name}' added.")
        return new_contact

    # search contact
    def search(self, name=None, phone_number=None):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                contacts = data.get("contacts", [])

                result = []
                for contact in contacts:
                    if (name and contact["name"].lower() == name.lower()) or \
                       (phone_number and contact["phone_number"] == phone_number):
                        result.append(contact)

                if result:
                    print("\nSearch result from file:")
                    for c in result:
                        print(f"Name: {c['name']}, Phone: {c['phone_number']}")
                else:
                    print("\nNo result found in file.")

        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON file.")


    # delete contact
        # delete contact by id or name
    def delete(self, id=None, name=None):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            contacts = data.get("contacts", [])
            original_len = len(contacts)

            contacts = [c for c in contacts if not (
                (id and c["id"] == id) or (name and c["name"].lower() == name.lower())
            )]

            deleted_count = original_len - len(contacts)

            if deleted_count > 0:
                with open(self.file_path, 'w', encoding='utf-8') as f:
                    json.dump({"contacts": contacts}, f, ensure_ascii=False, indent=4)
                print(f"{deleted_count} contact(s) deleted.")
                self.contact_list = contacts  
            else:
                print("No matching contact found to delete.")

        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON file.")


    
    # backup list contact
    def backup(self, backup_path="./contact_list_backup.json"):
        with open(backup_path, "w", encoding="utf-8") as f:
            json.dump(self.contact_list, f, ensure_ascii=False, indent=4)
        print(f" Backup saved to {backup_path}")

    #  display all contacts
    def display(self):
        print("\n Contact list:")
        for c in self.contact_list:
            print(f"{c['id']}. Name: {c['name']}\n   Phone: {c['phone_number']}")


# test system
con = ContactManager()
con.add(1, "John", "123456")
con.add(2, "rahimi", "789012")
con.search(name="Rahimi")
con.backup()
con.display()
