from hashlib import new
from unicodedata import name


class Things:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        new_item = Things(name, quantity, price)
        self.items.append(new_item)

    #ASK ABOUT THIS TOMORROW
    def delete(self, name, quantity, price):
        for return_item in self.items:
            if return_item in self.items:
                print(f"{return_item.name} has been removed")
                self.items.remove(return_item)

                print(self.items)

    def print_items(self):
        print("~===" * 7)

        print("SHOPPING CART")

        for item in self.items:
            print(item.name, item.quantity, item.price)


        print("~===" * 7)

    def run(self):
        while True:
            user_choice = input("What would you  like to do? (add/view/delete/quit):  ").lower()

            if user_choice == 'add':
                name = input("Product name: ")
                quantity = int(input("Product Quantity: "))
                price = int(input("Product Price: "))

                self.add_item(name, quantity, price)


            #ASK TEACHER TOMORROW!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
            elif user_choice == 'delete':
                self.print_items()

                name = input("Product name: ")
                quantity = int(input("Product Quantity: "))
                price = int(input("Product Price: "))



                self.delete(name, quantity, price)

            elif user_choice == 'view':
                self.print_items()
            
            elif user_choice == 'quit':
                self.print_items()
                break

ShopNow = Cart()
ShopNow.run()


