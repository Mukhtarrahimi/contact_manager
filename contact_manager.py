class ContactManager:
    def __init__(self):
        self.contact_list = []
        
    def add(self,id, name, phone_number):
        self.contact_list.append({"id":id,
                                  "name" :name,
                                  "phone_number" : phone_number})