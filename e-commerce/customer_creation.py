#Customer Creation and Processing
from customer import Customer

#Create a customer object
customer1 = Customer("John", "123 Main Street", "123456789")
print(customer1.get_details())

#Ask user if add customer or update customer
choice = input("Do you want to update the customer ? (y/n): ")
if choice.lower() == 'y':
    new_name = input("Enter the new name: ")
    new_address = input("Enter the new address: ")
    new_contact = input("Enter the new contact: ")
    customer1.update_name(new_name)
    customer1.update_address(new_address)
    customer1.update_contact(new_contact)
    print(customer1.get_details())
else:
    new_name = input("Enter the name: ")
    new_address = input("Enter the address: ")
    new_contact = input("Enter the contact: ")
    customer2 = Customer(new_name, new_address, new_contact)
    print(customer2.get_details())