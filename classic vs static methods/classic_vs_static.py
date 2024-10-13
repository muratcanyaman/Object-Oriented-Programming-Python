import csv
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

        # we access class level instance
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity

    def discount_price(self):
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    # This function opens a csv file and converts each line to dictionary,then converts to a list contains dictionaries.
    def instantiate_from_csv(cls):
        '''
        This should do something that has a relationship with the class.But usually, those are used to
        manipulate different structures of data to instantiate objects,like we have done with CSV file.
        :return:
        '''
        with open('items.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

        # We create our instances from here now
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))
            )

    @staticmethod
    def is_integer(num):
        '''
        This should do something that has a relationship with the class,but not something that must be unique per instance.
        '''
        if isinstance(num, float):
            return num.is_integer() # This is_integer() function is a built-in function in python.We don't call is_integer() method recursively here.
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"

Item.instantiate_from_csv()
print(Item.all)
