class Customer:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact


    def get_details(self):
        return f"Name: {self.name}, Address: {self.address}, Contact: {self.contact}"
    
    def update_name(self, new_name):
        self.name = new_name

    def update_address(self, new_address):
        self.address = new_address

    def update_contact(self, new_contact):
        self.contact = new_contact
    