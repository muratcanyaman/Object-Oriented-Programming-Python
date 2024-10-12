
class Item:
    # class level instance
    pay_rate = 0.8
    all = []

    def __init__(self ,name : str, price : float, quantity = 0):
        # We use assert in python for testing a condition.It returns error when condition is false.
        assert price >= 0, f"Price {price} is not greater than 0 or equal 0 !"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0 or equal 0 !"

        # instance level instances
        self.name = name
        self.price = price
        self.quantity = quantity

        # we access class level instance and append the items we created.
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity

    def discount_price(self):
        self.price = self.price * self.pay_rate
        return self.price
    
    # When we use print function each time this function runs automaticly and writes the console each item of the list.
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"


item1 = Item("Phone", 100, 3)
print(f"Discount Price of {item1.name}  : ", item1.discount_price())
print(f"Total Price of {item1.name} : ", item1.calculate_total_price())
item2 = Item("TV", 200, 4)
print(f"Discount Price of {item2.name} : ", item2.discount_price())
print(f"Total Price of {item2.name} : ", item2.calculate_total_price())
item3 = Item("Mouse", 1500, 1)
print(f"Discount Price of {item3.name} : ", item3.discount_price())
print(f"Total Price of {item3.name} : ", item3.calculate_total_price())
item4 = Item("Keyboard", 500, 2)
print(f"Discount Price of {item4.name} : ", item4.discount_price())
print(f"Total Price of {item4.name} : ", item4.calculate_total_price())
item5 = Item("Router", 300, 10)
print(f"Discount Price of {item5.name} : ", item5.discount_price())
print(f"Total Price of {item5.name} : ", item5.calculate_total_price())

print(f"Item list : ", Item.all)