import json

class ContactManager:
    def __init__(self):
        self.contact_list = []

    # function for add contact
    def add(self, id, name, phone_number):
        self.contact_list.append({
            "id": id,
            "name": name,
            "phone_number": phone_number
        })

    # function for search in contact list
    def search(self, name=None, phone_number=None):
        result = []
        for contact in self.contact_list:
            if (name and contact["name"].lower() == name.lower()) or \
               (phone_number and contact["phone_number"] == phone_number):
                result.append(contact)

        if result:
            print(" Result of search:")
            for c in result:
                print(f"Name: {c['name']}\nPhone: {c['phone_number']}")
        else:
            print(" No result found.")

    # function for backup contact list
    def backup(self, file_path="./contact_list.json"):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.contact_list, f, ensure_ascii=False, indent=4)
        print("Backup saved successfully.")

    # function for display contact list
    def display(self):
        print("\nContact list:")
        for c in self.contact_list:
            print(f"{c['id']}. Name: {c['name']}\n   Phone: {c['phone_number']}")


#  test system
con = ContactManager()
con.add(1, "John", "123456")
con.add(2, "rahimi", "789012")
con.search(name="Rahimi")
con.backup()
con.display()
