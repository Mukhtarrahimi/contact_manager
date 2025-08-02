class ContactManager:
    def __init__(self):
        self.contact_list = []
        

    # function for add contact
    def add(self,id, name, phone_number):
        self.contact_list.append({"id":id,
                                  "name" :name,
                                  "phone_number" : phone_number})
        
    # function for search in contact list
    def search(self, name= None, phone_number= None):
        result = []
        for contact in self.contact_list:
            if contact["name"].lower() == name or contact["phone_number"] == phone_number:
                result.append(contact)
                
        if result:
            print("result search:")
            for c in result:
                print(f"Name: {c['name']}\nphone: {c['phone_number']}")
        else:
            print("no result search")
        
    def display(self):
        print("Contact list")
        for c in self.contact_list:
            print(f"{c['id']}. Name: {c['name']}\n   phone: {c['phone_number']}")
            
            
        
con = ContactManager()
con.add(1, "John", "123456")
con.add(2, "rahimi", "789012")
con.search(name = "rahimi")
con.display()

