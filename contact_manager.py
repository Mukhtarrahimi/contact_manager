class ContactManager:
    def __init__(self):
        self.contact_list = []
        

    # function for add contact
    def add(self,id, name, phone_number):
        self.contact_list.append({"id":id,
                                  "name" :name,
                                  "phone_number" : phone_number})
        
    # function for search in contact list
    def search(self, name, phone_number):
        result = []
        for contact in enumerate(self.contact_list):
            if contact["name"] == name or contact["phone_number"] == phone_number:
                result.append(contact)
                
        print(result)