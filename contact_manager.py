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
        result = []
        for contact in self.contact_list:
            if (name and contact["name"].lower() == name.lower()) or \
               (phone_number and contact["phone_number"] == phone_number):
                result.append(contact)

        if result:
            print("\nResult of search:")
            for c in result:
                print(f"Name: {c['name']}\nPhone: {c['phone_number']}")
        else:
            print("\n No result found.")

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
