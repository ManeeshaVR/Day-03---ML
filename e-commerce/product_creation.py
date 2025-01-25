#Product Creation and Processing
from product import Product

#Create a product object
product1 = Product("Phone", 5000, 10)
print(product1.get_details())

#Update the price of the product
product1.update_price(5500)
print(product1.get_details())

#Ask user if add product or update product
choice = input("Do you want to update the product ? (y/n): ")
if choice.lower() == 'y':
    new_price = float(input("Enter the new price: "))
    product1.update_price(new_price)
    new_quantity = int(input("Enter the new quantity: "))
    product1.update_quantity(new_quantity)
    print(product1.get_details())
else:
    new_price = float(input("Enter the price: "))
    new_quantity = int(input("Enter the quantity: "))
    product2 = Product("Phone", new_price, new_quantity)
    print(product2.get_details())